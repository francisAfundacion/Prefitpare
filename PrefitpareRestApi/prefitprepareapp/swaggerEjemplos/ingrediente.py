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
                    "mensaje": "Ingrediente creada con éxito."
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
                "application/json": {"error": "No se encontró el ingrediente con el id especificado."}
            }
        )
    }
}

swagger_eliminar_ingrediente = {
    "operation_description": "Elimina una categoría por su ID.",
    "responses": {
        200: openapi.Response(
            description="Ingrediente eliminada con éxito.",
            examples={
                "application/json": {
                    "id": 5,
                    "mensaje": "Categoría eliminada con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Categoría no encontrada.",
            examples={
                "application/json": {"error": "No se encontró la categoría con el id especificado."}
            }
        )
    }
}