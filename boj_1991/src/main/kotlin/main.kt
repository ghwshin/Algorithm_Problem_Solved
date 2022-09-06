import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

class TreeNode(parent: TreeNode?, data: String) {
    lateinit var left: TreeNode
    lateinit var right: TreeNode

    fun addChild(l: String, r: String) {
        left = TreeNode(this, l)
        right = TreeNode(this, r)
    }

}

class Tree(root: TreeNode, n: Int) {

}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val t = StringTokenizer(br.readLine())
    val r = TreeNode(null, t.nextToken())
    r.addChild(t.nextToken(), t.nextToken())
    val tr = Tree(r, n)
    for (i: Int in 2..n) {

    }
}