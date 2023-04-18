"""Initial migration

Revision ID: 44820960416e
Revises: 
Create Date: 2023-04-18 16:41:19.263818

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite



# revision identifiers, used by Alembic.
revision = '44820960416e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planning',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('original_id', sa.VARCHAR(), nullable=False),
    sa.Column('talent_id', sa.VARCHAR(), nullable=True),
    sa.Column('talent_name', sa.VARCHAR(), nullable=True),
    sa.Column('talent_grade', sa.VARCHAR(), nullable=True),
    sa.Column('booking_grade', sa.VARCHAR(), nullable=True),
    sa.Column('operating_unit', sa.VARCHAR(), nullable=False),
    sa.Column('office_city', sa.VARCHAR(), nullable=True),
    sa.Column('office_postal_code', sa.VARCHAR(), nullable=False),
    sa.Column('job_manager_name', sa.VARCHAR(), nullable=True),
    sa.Column('job_manager_id', sa.VARCHAR(), nullable=True),
    sa.Column('total_hours', sa.FLOAT(), nullable=False),
    sa.Column('start_date', sa.DATETIME(), nullable=False),
    sa.Column('end_date', sa.DATETIME(), nullable=False),
    sa.Column('client_name', sa.VARCHAR(), nullable=True),
    sa.Column('client_id', sa.VARCHAR(), nullable=False),
    sa.Column('industry', sa.VARCHAR(), nullable=True),
    sa.Column('required_skills', sqlite.JSON(), nullable=True),
    sa.Column('optional_skills', sqlite.JSON(), nullable=True),
    sa.Column('is_unassigned', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('original_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planning')
    # ### end Alembic commands ###