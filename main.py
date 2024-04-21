import glob
import importlib.util
import os
import sys

from fastapi import APIRouter, FastAPI

from core.db.postgres.models import sync_models_with_database

# add the service folder to the path
service_fpath = os.path.join(os.path.dirname(__file__), "services", "**")
services_paths = glob.glob(service_fpath)
sys.path.extend(services_paths)

# database

router = APIRouter()

services_folder = "services"
for service_name in os.listdir(services_folder):
    if os.path.isdir(os.path.join(services_folder, service_name)) and os.path.exists(
        os.path.join(services_folder, service_name, "service.py")
    ):
        spec = importlib.util.spec_from_file_location(
            "service", f"{services_folder}/{service_name}/service.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "Service"):
            service_class = getattr(module, "Service")
            service_instance = service_class()

            if hasattr(service_instance, "get"):
                router.add_api_route(
                    f"/{service_name}",
                    getattr(service_instance, "get"),
                    methods=["GET"],
                )
            if hasattr(service_instance, "post"):
                router.add_api_route(
                    f"/{service_name}",
                    getattr(service_instance, "post"),
                    methods=["POST"],
                )
            if hasattr(service_instance, "put"):
                router.add_api_route(
                    f"/{service_name}",
                    getattr(service_instance, "put"),
                    methods=["PUT"],
                )
            if hasattr(service_instance, "delete"):
                router.add_api_route(
                    f"/{service_name}",
                    getattr(service_instance, "delete"),
                    methods=["DELETE"],
                )

        else:
            raise ValueError(f"Service class not found in {service_name}")
    else:
        raise ValueError(f"Service file not found in {service_name}")


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await sync_models_with_database()
