def get_filter_borrow(memberId: str = None, status: str = None, bookId: str = None):
    filter = {}
    if memberId:
        filter["userId"] = memberId
    if status:
        filter["status"] = status
    if bookId:
        filter["bookId"] = bookId
    return filter
