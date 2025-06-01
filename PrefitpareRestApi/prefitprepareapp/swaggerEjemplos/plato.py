from drf_yasg import openapi
from prefitprepareapp.serializadores.SerializadorPlato import SerializadorPlato

swagger_listar_platos= {
    "operation_description": "Devuelve una lista con todos los platos del sistema.",
    "responses": {
        200: openapi.Response(
            description="Lista de ingredientes.",
            schema=SerializadorPlato(many=True)
        )
    }
}

swagger_crear_plato = {
    "operation_description": "Crea un nuevo plato en el sistema.",
    "request_body": SerializadorPlato,
    "responses": {
        201: openapi.Response(
            description="Plato creado con éxito.",
            examples={
                "application/json": {
                    "id": 10,
                    "mensaje": "Plato creada con éxito."
                }
            }
        )
    }
}

swagger_modificar_plato = {
    "operation_description": "Modifica un nuevo plato del sistema acorde un ID especificado.",
    "request_body": SerializadorPlato,
    "responses": {
        200: openapi.Response(
            description="Plato modificado con éxito.",
            examples={
                "application/json": {
                    "id": 3,
                    "nombre_nuevo": "Nuevo plato",
                    "mensaje": "El plato ha sido actualizado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Plato no encontrado.",
            examples={
                "application/json": {"detail": "No existe el recurso/s solicitado/s acorde al id especificado"}
            }
        )
    }
}

swagger_eliminar_plato = {
    "operation_description": "Elimina un plato por su ID.",
    "responses": {
        200: openapi.Response(
            description="Plato eliminado con éxito.",
            examples={
                "application/json": {
                    "id": 5,
                    "mensaje": "Plato eliminado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Plato no encontrado.",
            examples={
                "application/json": {"detail": "No existe el recurso/s solicitado/s acorde al id especificado"}
            }
        )
    }
}