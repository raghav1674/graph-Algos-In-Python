package main
import "fmt"


func nthFibonacci(n int) int {

	if n==1 || n==2{
		return n-1
	}
	return nthFibonacci(n-1) + nthFibonacci(n-2)
}

var dp map[int]int

func memFibonacci(n int) int {


	if n==1 || n==2{
		return n-1
	}else if _,ok := dp[n]; !ok{

		dp[n] = memFibonacci(n-1) + memFibonacci(n-2)

	}

	return dp[n]


}

func top_down_fibonacci(n int )int{

	if n==1 || n ==2{

		return n-1
	}
	a := 0
	b := 1 

	for i:=2;i<n;i++{

		a,b  = b,a+b


	}
	return b

}


func main(){

	dp = make(map[int]int)

	fmt.Println(top_down_fibonacci(8))

}