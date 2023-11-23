from django.db.models import (
    CASCADE,
    RESTRICT,
    Model,
    DateField,
    FloatField,
    ForeignKey,
)


class UsageAnalysis(Model):
    analysis_start_date = DateField()
    analysis_end_date = DateField()
    date_created = DateField(auto_now_add=True)
    consumable = ForeignKey(to="data.Consumable", on_delete=CASCADE)
    assumed_rate = FloatField()
    actual_rate = FloatField()
    created_by = ForeignKey(to="accounts.CustomUser", on_delete=RESTRICT)

    def __repr__(self):
        return {
            "analysis_start_date": self.analysis_start_date,
            "analysis_end_date": self.analysis_end_date,
            "date_created": self.date_created,
            "consumable_analyzed": self.consumable,
        }
