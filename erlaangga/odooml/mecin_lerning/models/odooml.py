from odoo import models, fields


class Project(models.Model):
	_inherit = "project.task"

	price = fields.Float("Price")
	estimation = fields.Float("Estimation")


class Event(models.Model):
	_inherit = "event.event"

	price = fields.Float("Price")
	is_bootcamp = fields.Boolean("Bootcamp")


class BootcampCourse(models.Model):
	_name = "event.event.course"

	name = fields.Char("Name")
	course_datetime = fields.Datetime("Date")