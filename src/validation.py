def validate_order(order_dict: dict) -> tuple[bool, str]:
    """يرجع (صحيح؟, رسالة الخطأ لو في)"""
    
    required = ["n_items", "total_price", "total_freight", "n_payments", "total_payment"]
    for field in required:
        if field not in order_dict or order_dict[field] is None:
            return False, f"missing field: {field}"
    
    if order_dict["n_items"] <= 0:
        return False, "n_items must be positive"
    
    if order_dict["total_price"] < 0:
        return False, "total_price cannot be negative"
    
    if order_dict["total_price"] > 100000:
        return False, "total_price out of expected range"
    
    return True, ""
