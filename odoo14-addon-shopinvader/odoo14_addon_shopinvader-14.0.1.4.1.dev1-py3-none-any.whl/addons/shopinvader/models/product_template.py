# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from contextlib import contextmanager

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _search_shopinvader_backend_ids(self, operator, value):
        si_var_obj = self.env["shopinvader.product"]
        bindings = si_var_obj.search([("backend_id.name", operator, value)])

        return [("id", "in", bindings.mapped("record_id").ids)]

    shopinvader_bind_ids = fields.One2many(
        "shopinvader.product",
        "record_id",
        string="Shopinvader Binding",
        context={"active_test": False, "map_children": True},
    )

    shopinvader_backend_ids = fields.Many2many(
        string="ShopInvader Backends",
        comodel_name="shopinvader.backend",
        compute="_compute_shopinvader_backend_ids",
        store=False,
        search=_search_shopinvader_backend_ids,
    )

    active = fields.Boolean(inverse="_inverse_active")

    def _inverse_active(self):
        inactive = self.filtered(lambda p: not p.active)
        inactive.mapped("shopinvader_bind_ids").write({"active": False})

    def _compute_shopinvader_backend_ids(self):
        for rec in self:
            rec.shopinvader_backend_ids = rec.mapped("shopinvader_bind_ids.backend_id")

    def unlink(self):
        for record in self:
            # TODO we should propose to redirect the old url
            record.shopinvader_bind_ids.unlink()
        return super(ProductTemplate, self).unlink()

    @contextmanager
    def _manage_name_update(self):
        """
        When the product name is updated, re-sync url
        :return:
        """
        self_name = {r: r.name for r in self}
        yield
        for record in self:
            if not record.sudo().shopinvader_bind_ids:
                continue
            if record.name != self_name.get(record):
                record.sudo().shopinvader_bind_ids._sync_urls()

    def write(self, vals):
        """
        Inherit the write to re-sync url if necessary
        :param vals: dict
        :return: bool
        """
        with self._manage_name_update():
            result = super(ProductTemplate, self).write(vals)
        return result
