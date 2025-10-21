import pytest
from main import BSTNode
from user import User, get_users


class TestBSTNodeInsert:
  """Test suite for the BSTNode.insert() method"""

  def test_insert_3_users(self):
    """Test inserting 3 users into BST"""
    # Arrange
    num_users = 3
    users = get_users(num_users)
    bst = BSTNode()
    
    # Act
    for user in users:
      bst.insert(user)
    
    # Assert
    inorder = self._get_inorder_traversal(bst)
    sorted_users = sorted(users)
    
    assert len(inorder) == num_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 3 Users\n"
      f"{'='*70}\n"
      f"📊 Expected {num_users} nodes in tree\n"
      f"❌ Got:      {len(inorder)} nodes\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"{'='*70}\n"
    )
    
    assert inorder == sorted_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 3 Users - Invalid BST Property\n"
      f"{'='*70}\n"
      f"📊 Users inserted: {[str(u) for u in users]}\n"
      f"✅ Expected (sorted): {[str(u) for u in sorted_users]}\n"
      f"❌ Got (in-order):    {[str(u) for u in inorder]}\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"💡 In-order traversal should produce sorted output\n"
      f"{'='*70}\n"
    )

  def test_insert_5_users(self):
    """Test inserting 5 users into BST"""
    # Arrange
    num_users = 5
    users = get_users(num_users)
    bst = BSTNode()
    
    # Act
    for user in users:
      bst.insert(user)
    
    # Assert
    inorder = self._get_inorder_traversal(bst)
    sorted_users = sorted(users)
    
    assert len(inorder) == num_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 5 Users\n"
      f"{'='*70}\n"
      f"📊 Expected {num_users} nodes in tree\n"
      f"❌ Got:      {len(inorder)} nodes\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"{'='*70}\n"
    )
    
    assert inorder == sorted_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 5 Users - Invalid BST Property\n"
      f"{'='*70}\n"
      f"📊 Users inserted: {[str(u) for u in users]}\n"
      f"✅ Expected (sorted): {[str(u) for u in sorted_users]}\n"
      f"❌ Got (in-order):    {[str(u) for u in inorder]}\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"💡 In-order traversal should produce sorted output\n"
      f"{'='*70}\n"
    )

  def test_insert_10_users(self):
    """Test inserting 10 users into BST"""
    # Arrange
    num_users = 10
    users = get_users(num_users)
    bst = BSTNode()
    
    # Act
    for user in users:
      bst.insert(user)
    
    # Assert
    inorder = self._get_inorder_traversal(bst)
    sorted_users = sorted(users)
    
    assert len(inorder) == num_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 10 Users\n"
      f"{'='*70}\n"
      f"📊 Expected {num_users} nodes in tree\n"
      f"❌ Got:      {len(inorder)} nodes\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"{'='*70}\n"
    )
    
    assert inorder == sorted_users, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert 10 Users - Invalid BST Property\n"
      f"{'='*70}\n"
      f"📊 Users inserted: {[str(u) for u in users]}\n"
      f"✅ Expected (sorted): {[str(u) for u in sorted_users]}\n"
      f"❌ Got (in-order):    {[str(u) for u in inorder]}\n"
      f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
      f"💡 In-order traversal should produce sorted output\n"
      f"{'='*70}\n"
    )

  def test_insert_empty_tree(self):
    """Test inserting into empty tree sets root"""
    # Arrange
    bst = BSTNode()
    user = User(42)
    
    # Act
    bst.insert(user)
    
    # Assert
    assert bst.val == user, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert Into Empty Tree\n"
      f"{'='*70}\n"
      f"✅ Expected root: {user}\n"
      f"❌ Got:          {bst.val}\n"
      f"💡 First insert should set the root value\n"
      f"{'='*70}\n"
    )
    assert bst.left is None and bst.right is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert Into Empty Tree - Children Should Be None\n"
      f"{'='*70}\n"
      f"❌ Left child:  {bst.left}\n"
      f"❌ Right child: {bst.right}\n"
      f"💡 Single node should have no children\n"
      f"{'='*70}\n"
    )

  def test_insert_duplicate_user(self):
    """Test inserting duplicate users doesn't add them twice"""
    # Arrange
    bst = BSTNode()
    user1 = User(5)
    user2 = User(3)
    user3 = User(5)  # Duplicate of user1
    
    # Act
    bst.insert(user1)
    bst.insert(user2)
    bst.insert(user3)
    
    # Assert
    inorder = self._get_inorder_traversal(bst)
    assert len(inorder) == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Insert Duplicate User\n"
      f"{'='*70}\n"
      f"📊 Inserted: {user1}, {user2}, {user3} (duplicate)\n"
      f"✅ Expected: 2 unique nodes\n"
      f"❌ Got:      {len(inorder)} nodes\n"
      f"🌳 In-order: {[str(u) for u in inorder]}\n"
      f"💡 BST should not add duplicate values\n"
      f"{'='*70}\n"
    )

  def test_bst_property_left_less_than_root(self):
    """Test that left subtree contains only smaller values"""
    # Arrange
    bst = BSTNode()
    users = [User(10), User(5), User(3), User(7)]
    
    # Act
    for user in users:
      bst.insert(user)
    
    # Assert
    root_val = bst.val
    if bst.left:
      left_subtree = self._get_inorder_traversal(bst.left)
      for user in left_subtree:
        assert user < root_val, (
          f"\n{'='*70}\n"
          f"❌ TEST FAILED: BST Property Violation - Left Subtree\n"
          f"{'='*70}\n"
          f"📊 Root value: {root_val}\n"
          f"❌ Found in left subtree: {user}\n"
          f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
          f"💡 All left subtree values must be < root\n"
          f"{'='*70}\n"
        )

  def test_bst_property_right_greater_than_root(self):
    """Test that right subtree contains only larger values"""
    # Arrange
    bst = BSTNode()
    users = [User(10), User(15), User(12), User(20)]
    
    # Act
    for user in users:
      bst.insert(user)
    
    # Assert
    root_val = bst.val
    if bst.right:
      right_subtree = self._get_inorder_traversal(bst.right)
      for user in right_subtree:
        assert user > root_val, (
          f"\n{'='*70}\n"
          f"❌ TEST FAILED: BST Property Violation - Right Subtree\n"
          f"{'='*70}\n"
          f"📊 Root value: {root_val}\n"
          f"❌ Found in right subtree: {user}\n"
          f"🌳 Tree structure:\n{self._format_tree(bst)}\n"
          f"💡 All right subtree values must be > root\n"
          f"{'='*70}\n"
        )

  # Helper methods
  def _get_inorder_traversal(self, node):
    """Get in-order traversal of BST (should be sorted)"""
    result = []
    self._inorder_helper(node, result)
    return result
  
  def _inorder_helper(self, node, result):
    """Recursive helper for in-order traversal"""
    if node is None or node.val is None:
      return
    self._inorder_helper(node.left, result)
    result.append(node.val)
    self._inorder_helper(node.right, result)
  
  def _format_tree(self, node, level=0):
    """Format tree structure for display"""
    if node is None or node.val is None:
      return ""
    
    lines = []
    # Right subtree (printed on top)
    if node.right:
      lines.append(self._format_tree(node.right, level + 1))
    
    # Current node
    lines.append("    " * level + "> " + str(node.val))
    
    # Left subtree (printed on bottom)
    if node.left:
      lines.append(self._format_tree(node.left, level + 1))
    
    return "\n".join(filter(None, lines))
