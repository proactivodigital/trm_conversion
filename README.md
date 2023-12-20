# Módulo de Conversión de Precios a Monedas en Odoo
Este módulo personalizado para Odoo simplifica la conversión de precios de productos a diferentes monedas, mejorando la flexibilidad en la gestión y visualización de los precios en entornos multinacionales.

# Características Principales
# Conversión Directa de Monedas:
Añade dos campos adicionales para especificar la moneda de origen (from_currency_id) y la moneda de destino (to_currency_id) al crear o modificar un producto.

# Visualización Clara de Precios Convertidos:
Personaliza la vista de productos para incluir información sobre la moneda de origen y la moneda de destino, ofreciendo una visión clara de la relación de conversión.

# Instalación
Clona este repositorio en tu entorno de desarrollo Odoo.
Agrega y confirma los cambios al repositorio Git.
Realiza un push del código a tu rama principal en Odoo.sh.

# Uso
1. Después de instalar el módulo, accede al menú de productos en tu instancia de Odoo.
2. Al crear o editar una factura, verás nuevos campos adicionales para especificar la moneda de origen y la fecha de la que obtendras el trm.
3. Los precios del producto se calcularán automáticamente según las tasas de conversión establecidas entre las monedas seleccionadas.