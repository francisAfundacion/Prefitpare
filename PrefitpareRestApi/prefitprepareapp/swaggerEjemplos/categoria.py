from drf_yasg import openapi
from prefitprepareapp.serializadores.SerializadorCategoria import SerializadorCategoria

swagger_listar_categorias = {
    "operation_description": "Devuelve una lista con todas las categorías registradas.",
    "responses": {
        200: openapi.Response(
            description="Lista de categorías.",
            schema=SerializadorCategoria(many=True)
        )
    }
}

swagger_crear_categoria = {
    "operation_description": "Crea una nueva categoría en el sistema.",
    "request_body": SerializadorCategoria,
    "responses": {
        201: openapi.Response(
            description="Categoría creada con éxito.",
            examples={
                "application/json": {
                    "id": 10,
                    "mensaje": "Categoría creada con éxito."
                }
            }
        )
    }
}

swagger_modificar_categoria = {
    "operation_description": "Modifica una categoría del sistema acorde un ID especificado.",
    "request_body": SerializadorCategoria,
    "responses": {
        200: openapi.Response(
            description="Categoría modificada con éxito.",
            examples={
                "application/json": {
                    "id": 3,
                    "nombre_nuevo": "Nueva categoría",
                    "mensaje": "El producto ha sido actualizado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Categoría no encontrada.",
            examples={
                "application/json": {"error": "No se encontró la categoría."}
            }
        )
    }
}

swagger_eliminar_categoria = {
    "operation_description": "Elimina una categoría por su ID.",
    "responses": {
        200: openapi.Response(
            description="Categoría eliminada con éxito.",
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
                "application/json": {"error": "No se encontró la categoría."}
            }
        )
    }
}