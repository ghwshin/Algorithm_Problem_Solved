import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ListResourceBundle
import java.util.StringTokenizer

class Graph(private val n: Int) {
    val g: List<List<Int>>
    val rb = BufferedReader(InputStreamReader(System.`in`))
    init {
        g = List<List<Int>>(n + 1, { List<Int> (0, { 0 })})
        for (i: Int in 1..n) {
            g.plus(rb.readLine().split(" ").map { it.toInt() })
        }
    }


    fun read() {
    }
}

fun main() {
    val rb = BufferedReader(InputStreamReader(System.`in`))
    val g = Graph(rb.readLine().toInt())
    g.read()

}