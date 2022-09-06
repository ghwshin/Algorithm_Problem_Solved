import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.StringTokenizer
import kotlin.math.abs

class Nqueen {
    lateinit var col: Array<Int>
    var n = 0
    var cnt = 0

    fun initqueen(_n: Int) {
        n = _n
        col = Array<Int>(_n + 1) { 0 }
    }

    fun queens(i: Int) {
        if (promising(i)) {
            if (i == n) {
                cnt += 1
            }
            else {
                for (j: Int in 1..n) {
                    col[i + 1] = j
                    queens(i + 1)
                }
            }
        }
    }

    fun promising(i: Int) : Boolean {
        var k: Int = 1
        var sw: Boolean = true
        while (k < i && sw) {
            if (col[i] == col[k] || abs(col[i] - col[k]) == i - k)
                sw = false
            k += 1
        }
        return sw
    }
}

fun main() {
    val rb = BufferedReader(InputStreamReader(System.`in`))
    val rw = BufferedWriter(OutputStreamWriter(System.out))
    val n = StringTokenizer(rb.readLine()).nextToken().toInt()
    val nq = Nqueen()
    nq.initqueen(n)
    nq.queens(0)
    println(nq.cnt)
}