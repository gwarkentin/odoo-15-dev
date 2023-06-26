# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    short_name = fields.Char('Short Title')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    color = fields.Integer()
    image = fields.Binary(attachment=True)
    html_description = fields.Html()
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        'State', default="draft")
    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue

    def make_available(self):
        #self.change_state('available')
        self.change_state('draft') #Ning: this is a bug

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')
