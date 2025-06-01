from drf_yasg import openapi
from prefitprepareapp.serializadores.SerializadorIngrediente import SerializadorIngrediente

swagger_listar_ingredientes= {
    "operation_description": "Devuelve una lista con todos los ingredientes del sistema.",
    "responses": {
        200: openapi.Response(
            description="Lista de ingredientes.",
            schema=SerializadorIngrediente(many=True)
        )
    }
}

swagger_crear_ingrediente = {
    "operation_description": "Crea un nuevo ingrediente en el sistema.",
    "request_body": SerializadorIngrediente,
    "responses": {
        201: openapi.Response(
            description="Ingrediente creado con éxito.",
            examples={
                "application/json": {
                    "id": 10,
                    "mensaje": "Ingrediente creado con éxito."
                }
            }
        )
    }
}

swagger_modificar_ingrediente = {
    "operation_description": "Modifica un ingrediente del sistema.",
    "request_body": SerializadorIngrediente,
    "responses": {
        200: openapi.Response(
            description="Ingrediente modificado con éxito.",
            examples={
                "application/json": {
                    "id": 3,
                    "nombre_nuevo": "Nuevo ingrediente",
                    "mensaje": "El ingrediente ha sido actualizado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Ingrediente no encontrado.",
            examples={
                "application/json": {"detail": "No existe el recurso/s solicitado/s acorde al id especificado"}
            }
        )
    }
}

swagger_eliminar_ingrediente = {
    "operation_description": "Elimina un ingrediente por su ID.",
    "responses": {
        200: openapi.Response(
            description="Ingrediente eliminado con éxito.",
            examples={
                "application/json": {
                    "id": 5,
                    "mensaje": "Ingrediente eliminado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Ingrediente no encontrado.",
            examples={
                "application/json": {"detail": "No existe el recurso/s solicitado/s acorde al id especificado"}
            }
        )
    }
}