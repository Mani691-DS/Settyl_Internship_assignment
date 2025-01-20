# Settyl_Internship_assignment
This project has two files model.py, streamlit_app.py. Below is the explanation for ### model.py

---

### **Recommendation System Workflow**

The code implements a **hybrid recommendation system** that combines collaborative filtering, content-based filtering, and additional techniques for personalized recommendations.

---

### **Functions**

1. **`collaborative_filtering(user_id, purchases, browsing_history, products)`**
   - **Logic**: 
     - Finds products purchased by users with similar purchasing behavior to the target user.
     - Excludes products the target user has already purchased.
   - **Output**: Recommendations labeled as `"Collaborative Filtering"`.

2. **`content_based_filtering(user_id, purchases, browsing_history, products)`**
   - **Logic**:
     - Suggests products from the same categories as those browsed by the user.
     - Excludes previously browsed products.
   - **Output**: Recommendations labeled as `"Content-Based Filtering"`.
   - **Fallback**: Returns an empty DataFrame if no browsing history exists.

3. **`hybrid_recommendation(user_id, purchases, browsing_history, products)`**
   - **Steps**:
     1. Combines results from collaborative and content-based filtering.
     2. Adds **random unseen products** (not in the user's history) to diversify recommendations.
     3. Includes **popular products** (top 5 purchased).
   - **Final Output**: A deduplicated DataFrame with recommendations from multiple sources:
     - `"Collaborative Filtering"`, `"Content-Based Filtering"`, `"Random Unseen Products"`, `"Popular Products"`.

---

### **Key Points**
- **Avoids duplicates**: Uses `drop_duplicates()` on `product_id` to ensure unique recommendations.
- **Diverse recommendations**: Combines user-specific, category-specific, and general product suggestions.
- **Issues Fixed**:
  - Corrected typo: `prduct_id` → `product_id`.
  - Removed unnecessary `print()` statements.

---


