def get_filter_borrow(memberId: str = None, status: str = None):
    filter = {}
    if memberId:
        filter["userId"] = memberId
    if status:
        filter["status"] = status
    return filter
