from pydantic import BaseModel


class BusinessSettingsSchema(BaseModel):
    name: str
    value: str


class BusinessSettingsCreateSchema(BusinessSettingsSchema):
    ...


class BusinessSettingsUpdateSchema(BusinessSettingsSchema):
    name: str | None = None
    value: str | None = None


class BusinessSettingsReadSchema(BusinessSettingsSchema):
    ...
