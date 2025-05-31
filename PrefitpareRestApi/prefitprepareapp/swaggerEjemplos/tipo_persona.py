from drf_yasg import openapi
from prefitprepareapp.serializadores.SerializadorTipoPersona import SerializadorTipoPersona

swagger_listar_tipos_persona= {
    "operation_description": "Devuelve una lista con todos los tipos de persona del sistema.",
    "responses": {
        200: openapi.Response(
            description="Lista de tipos de persona.",
            schema=SerializadorTipoPersona(many=True)
        )
    }
}

swagger_crear_tipo_persona = {
    "operation_description": "Crea un nuevo tipo de persona en el sistema.",
    "request_body": SerializadorTipoPersona,
    "responses": {
        201: openapi.Response(
            description="Tipo de persona creado con éxito.",
            examples={
                "application/json": {
                    "id": 10,
                    "mensaje": "Tipo de persona creada con éxito."
                }
            }
        )
    }
}

swagger_modificar_tipo_persona = {
    "operation_description": "Modifica un tipo de persona del sistema acorde un ID especificado.",
    "request_body": SerializadorTipoPersona,
    "responses": {
        200: openapi.Response(
            description="Tipo de persona modificado con éxito.",
            examples={
                "application/json": {
                    "id": 3,
                    "nombre_nuevo": "Nuevo tipo de persona",
                    "mensaje": "El tipo de persona ha sido actualizado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Tipo de persona no encontrado.",
            examples={
                "application/json": {"error": "No se encontró el tipo de persona con el ID especificado."}
            }
        )
    }
}

swagger_eliminar_tipo_persona = {
    "operation_description": "Elimina un tipo de persona por su ID.",
    "responses": {
        200: openapi.Response(
            description="Tipo de persona eliminado con éxito.",
            examples={
                "application/json": {
                    "id": 5,
                    "mensaje": "Tipo de persona eliminado con éxito."
                }
            }
        ),
        404: openapi.Response(
            description="Tipo de persona no encontrada.",
            examples={
                "application/json": {"error": "No se encontró el tipo de persona con el ID especificado."}
            }
        )
    }
}