from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "001"
down_revision = None

def upgrade():
    op.create_table(
        "sport_types",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("unit", sa.String),
        sa.Column("world_record", sa.Numeric),
        sa.Column("olympic_record", sa.Numeric),
    )

    op.create_table(
        "athletes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("full_name", sa.String, nullable=False),
        sa.Column("country", sa.String),
        sa.Column("birth_year", sa.Integer),
        sa.Column("wins_count", sa.Integer, server_default="0"),
        sa.Column("profile", JSONB),
    )

    op.create_table(
        "results",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("competition_name", sa.String),
        sa.Column("event_date", sa.Date),
        sa.Column("event_place", sa.String),
        sa.Column("place", sa.Integer),
        sa.Column("result_value", sa.Numeric),
        sa.Column("sport_type_id", sa.Integer, sa.ForeignKey("sport_types.id")),
        sa.Column("athlete_id", sa.Integer, sa.ForeignKey("athletes.id")),
    )

def downgrade():
    op.drop_table("results")
    op.drop_table("athletes")
    op.drop_table("sport_types")
