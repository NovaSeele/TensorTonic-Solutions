def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    # Lấy top-k
    top_k = recommended[:k]
    # Chuyển relevant sang set để tối ưu tìm kiếm O(1)
    relevant_set = set(relevant)
    # Đếm số hits
    hits = sum(1 for item in top_k if item in relevant_set)
    # Tính precision và recall
    precision = hits / k
    recall = hits / len(relevant_set)
    
    return [precision, recall]