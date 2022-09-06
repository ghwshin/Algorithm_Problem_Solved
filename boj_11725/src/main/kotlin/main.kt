class TreeNode(parent: TreeNode?, data: Int) {
    lateinit var left: TreeNode
    lateinit var right: TreeNode

    fun addChild()

}

class Tree() {
    val root = TreeNode(null, 1)

}

fun main() {
    val t = Tree()
}