from . import orders, order_items, order_tracking, menu_items, promo_codes, payment, data_analysis, System_doc, customer_feedback, guest_checkout

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    order_tracking.Base.metadata.create_all(engine)
    promo_codes.Base.metadata.create_all(engine)
    data_analysis.Base.metadata.create_all(engine)
    System_doc.Base.metadata.create_all(engine)
    customer_feedback.Base.metadata.create_all(engine)
    guest_checkout.Base.metadata.create_all(engine)
