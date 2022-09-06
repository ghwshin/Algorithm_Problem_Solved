import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

class Virus (val n: Int, val c_num: Int) {
    val adj = Array<Array<Int>>(n + 1) { Array<Int>(n + 1) { 0 } }
    var cnt = 0
    val checked = Array<Boolean>(n + 1, { false });

    fun insert(x: Int, y: Int) {
        adj[x][y] = 1
        adj[y][x] = 1
    }

    fun dfs(target: Int) {
        checked[target] = true
        cnt += 1
        for (i: Int in 2..n) {
            if (checked[i] != true && adj[target][i] == 1) {
                dfs(i)
            }
        }
    }
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val c = br.readLine().toInt()
    val v_inst = Virus(n, c)
    for (i: Int in 1..c) {
        val tmp = StringTokenizer(br.readLine())
        v_inst.insert(tmp.nextToken().toInt(), tmp.nextToken().toInt())
    }
    v_inst.dfs(1)
    println(v_inst.cnt - 1)
}