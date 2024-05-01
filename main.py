# import importlib.util
# import os

# from fastapi import APIRouter, FastAPI

# from core.db.postgres.models import sync_models_with_database

# router = APIRouter()


# def service_name_validation(name: str) -> None | ValueError:
#     if (
#         " " in name
#         or name[0].isdigit()
#         or "/" in name
#         or "\\" in name
#         or "." in name
#         or ":" in name
#         or "?" in name
#         or '"' in name
#         or "<" in name
#         or ">" in name
#         or "|" in name
#         or "*" in name
#         or "[" in name
#         or "]" in name
#         or "=" in name
#         or ";" in name
#         or "," in name
#         or "!" in name
#         or "@" in name
#         or "#" in name
#         or "$" in name
#         or "%" in name
#         or "^" in name
#         or "&" in name
#         or "(" in name
#         or ")" in name
#         or "{" in name
#         or "}" in name
#         or "+" in name
#         or "`" in name
#         or "~" in name
#         or "'" in name
#     ):
#         raise ValueError(
#             f"Service name: {service_name} should contain only alphabets, numbers and underscores."
#         )


# def endpoint_friendly_service_name(name: str) -> str:
#     return name.replace("_", "-")


# services_folder = "services"
# for service_name in os.listdir(services_folder):
#     # validate service name
#     service_name_validation(service_name)

#     if os.path.isdir(os.path.join(services_folder, service_name)) and os.path.exists(
#         os.path.join(services_folder, service_name, "service.py")
#     ):
#         spec = importlib.util.spec_from_file_location(
#             "service", f"{services_folder}/{service_name}/service.py"
#         )
#         module = importlib.util.module_from_spec(spec)
#         module.__package__ = f"services.{service_name}"
#         spec.loader.exec_module(module)

#         if hasattr(module, "Service"):
#             service_class = getattr(module, "Service")
#             service_instance = service_class()
#             if hasattr(service_instance, "get"):
#                 router.add_api_route(
#                     f"/{service_name}",
#                     getattr(service_instance, "get"),
#                     methods=["GET"],
#                 )
#             if hasattr(service_instance, "post"):
#                 router.add_api_route(
#                     f"/{service_name}",
#                     getattr(service_instance, "post"),
#                     methods=["POST"],
#                 )
#             if hasattr(service_instance, "put"):
#                 router.add_api_route(
#                     f"/{service_name}",
#                     getattr(service_instance, "put"),
#                     methods=["PUT"],
#                 )
#             if hasattr(service_instance, "delete"):
#                 router.add_api_route(
#                     f"/{service_name}",
#                     getattr(service_instance, "delete"),
#                     methods=["DELETE"],
#                 )
#         else:
#             raise ValueError(f"Service class not found in {service_name}")
#     else:
#         raise ValueError(f"Service file not found in {service_name}")


# app = FastAPI()
# app.include_router(router)


# @app.on_event("startup")
# async def startup_event():
#     await sync_models_with_database()

from core.main import Singularity

app = Singularity()
