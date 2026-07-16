from fastapi import FastAPI
from . import orders, order_items, payment, order_tracking

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_items.router)
    app.include_router(order_tracking.router)
    app.include_router(payment.router)
