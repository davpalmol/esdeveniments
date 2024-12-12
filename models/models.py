# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.fields import Many2many


class esdeveniments(models.Model):
    _name = 'esdeveniments.esdeveniments'
    _description = 'esdeveniments.esdeveniments'

    name = fields.Char(string="Nombre del Evento")
    dataInici = fields.Date(string="Fecha de Inicio", default=fields.Datetime.now)
    dataFinal = fields.Date(string="Fecha de Fin", default=fields.Datetime.now)
    lloc = fields.Char(string="Ubicación")
    descpripcio = fields.Text(string="Descripción")
    foto = fields.Image(string="Foto", width=100)
    maximo_participantes = fields.Integer(string="Máximo de Participantes", default=10)
    participantes_ids = fields.Many2many('res.partner', string="Participantes")
    tipus = fields.Selection(
        [('conferencia', 'Conferencia'),
         ('taller', 'Taller'),
         ('seminario', 'Seminario')],
        string="Tipo de Evento"
    )
    duracion = fields.Integer(string="Duración (días)", compute='_compute_duracion', store=True)

    @api.depends('dataInici', 'dataFinal')
    def _compute_duracion(self):
        for record in self:
            if record.dataInici and record.dataFinal:
                # Calculamos la duración en días
                start_date = fields.Date.from_string(record.dataInici)
                end_date = fields.Date.from_string(record.dataFinal)
                # Aseguramos que la fecha de fin es mayor o igual a la de inicio
                record.duracion = (end_date - start_date).days
            else:
                record.duracion = 0

    @api.constrains('dataInici', 'dataFinal')
    def _check_fechas(self):
        for record in self:
            if record.dataFinal < record.dataInici:
                raise ValidationError("La fecha de fin debe ser igual o posterior a la fecha de inicio.")

    @api.constrains('participantes_ids', 'maximo_participantes')
    def _check_maximo_participantes(self):
        for record in self:
            if len(record.participantes_ids) > record.maximo_participantes:
                raise ValidationError("El número de participantes supera el límite permitido.")


class participants(models.Model):
    _name = 'esdeveniments.participants'
    _description = 'esdeveniments.participants'

    name = fields.Char()
    cognom = fields.Char()

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

