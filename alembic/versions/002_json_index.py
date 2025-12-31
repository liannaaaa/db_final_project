from alembic import op

revision = "002"
down_revision = "001"

def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    op.execute(
        "CREATE INDEX idx_profile_gin ON athletes USING GIN (profile jsonb_path_ops)"
    )

def downgrade():
    op.execute("DROP INDEX idx_profile_gin")
