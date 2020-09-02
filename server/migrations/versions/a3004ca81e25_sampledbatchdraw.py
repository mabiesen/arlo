# pylint: disable=invalid-name
"""SampledBatchDraw

Revision ID: a3004ca81e25
Revises: 11e35dd1c515
Create Date: 2020-08-25 22:38:13.118998+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a3004ca81e25"
down_revision = "11e35dd1c515"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sampled_batch_draw",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("batch_id", sa.String(length=200), nullable=False),
        sa.Column("round_id", sa.String(length=200), nullable=False),
        sa.Column("ticket_number", sa.String(length=200), nullable=False),
        sa.ForeignKeyConstraint(
            ["batch_id"],
            ["batch.id"],
            name=op.f("sampled_batch_draw_batch_id_fkey"),
            ondelete="cascade",
        ),
        sa.ForeignKeyConstraint(
            ["round_id"],
            ["round.id"],
            name=op.f("sampled_batch_draw_round_id_fkey"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint(
            "batch_id",
            "round_id",
            "ticket_number",
            name=op.f("sampled_batch_draw_pkey"),
        ),
    )

    op.add_column(
        "batch", sa.Column("audit_board_id", sa.String(length=200), nullable=True)
    )
    op.create_foreign_key(
        op.f("batch_audit_board_id_fkey"),
        "batch",
        "audit_board",
        ["audit_board_id"],
        ["id"],
        ondelete="cascade",
    )
    # ### end Alembic commands ###


def downgrade():  # pragma: no cover
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table("sampled_batch_draw")
    # ### end Alembic commands ###