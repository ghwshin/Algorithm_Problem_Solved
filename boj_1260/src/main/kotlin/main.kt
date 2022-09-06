import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.LinkedList
import java.util.Queue
import java.util.StringTokenizer

class Graph {
    lateinit var adj : Array<Array<Int>>
    lateinit var checked : Array<Boolean>
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    fun closeBuffer() {
        bw.close()
    }

    fun printBuffer() {
        bw.write("\n")
        bw.flush()
    }

    fun initMatrix(n : Int) {
        adj = Array<Array<Int>>(n + 1) { Array<Int>(n + 1) { 0 } }
        checked = Array<Boolean>(n + 1) { false }
    }

    fun checkInit(n : Int) {
        checked = Array<Boolean>(n + 1) { false }
    }

    fun addLine(start: Int, end: Int) {
        adj[start][end] = 1;
        adj[end][start] = 1;
    }

    fun dfs(n: Int, check: Int) {
        checked[check] = true
        bw.write("$check ")
        for (i: Int in 1 until n + 1) {
            if (adj[check][i] == 1 && checked[i] == false) {
                dfs(n, i)
            }
        }
    }

    fun bfs(n: Int, check:Int) {
        val bfsQueue: Queue<Int> = LinkedList()
        checked[check] = true
        bw.write("$check ")
        bfsQueue.add(check)
        while (!bfsQueue.isEmpty()) {
            val nextNode = bfsQueue.remove()
            for (i: Int in 1 until n + 1) {
                if (adj[nextNode][i] == 1 && checked[i] == false) {
                    bfsQueue.add(i)
                    checked[i] = true
                    bw.write("$i ")
                }
            }
        }
    }
}

fun main() {
    val instanceGraph = Graph()
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n: Int
    val m: Int
    val v: Int
    var token = StringTokenizer(br.readLine())
    n = token.nextToken().toInt()
    m = token.nextToken().toInt()
    v = token.nextToken().toInt()
    instanceGraph.initMatrix(n)
    repeat(m) {
        token = StringTokenizer(br.readLine())
        val s = token.nextToken().toInt()
        val e = token.nextToken().toInt()
        instanceGraph.addLine(s, e)
    }

    instanceGraph.dfs(n, v)
    instanceGraph.printBuffer()
    instanceGraph.checkInit(n)
    instanceGraph.bfs(n, v)
    instanceGraph.printBuffer()
    instanceGraph.closeBuffer()
}