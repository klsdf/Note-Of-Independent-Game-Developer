#  杨辉三角

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

```pseudocode
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```





思路：这个很简单啊，首先把第一行初始化为1，之后，第n行就有n个数字，除了开头和结尾为1以外，第num个数字值为上一行num-1和num的和。比如说第三行1位置的2，这个值就是第二行的0和1位置的数值相加。主要的结构就是二维数组。

语言：JavaScript

```javascript
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  if(numRows==0)
    return[];
  numRows-=1;//把行数转换为0开始，方便计算
  var result = new Array();

  //第一行是特例，默认为1
  result[0] = new Array(0)
  result[0].push(1);

  for(let row=1;row<=numRows;row++){
    result[row]= new Array();//为每一行都要新增一个动态数组。
    for(let num=0;num<=row;num++){
      if(num==0||num==row)
        result[row].push(1);//开头结尾默认为1
      else
        result[row].push(result[row-1][num-1]+result[row-1][num]);//拿到上一行的num-1和num位置的数
    }
  }
  return result;
};
```

# 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。所有输入只包含小写字母 `a-z` 。

```pseudocode
输入: ["flower","flow","flight"]
输出: "fl"

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
```



思路：**注意，重点是前缀，并不是最长公共子序列**。抖机灵想出来的，为了防止数组越界，我直接while（1），让他必定越界，这时就说明已经比较完了（或者说最短的那个string已经被榨干了。。。），此时只要来一个异常处理就可以了，直接返回之前保存的那个字符串。为了防止开局给空数组，所以try要在compare=strs[0].charAt(0);之前。剩下的就很容易看懂了。

语言：java

```java
class Solution {
 public String longestCommonPrefix(String[] strs) {
     String save="";//save保存的就是最长子序列
     try {
         
     //compare是用于比较的，默认取第一个字符串的第一个字符作为起始  
		 char compare=strs[0].charAt(0);
		 int index=0;
	 
		 while(true){//一直循环，如果越界，说明最长公共前缀就是最短的那个字符串
	    	for(String i:strs){//遍历每个字符串
	    		if(compare!=i.charAt(index))
	    			return save;//如果发现，不相等了，直接return，强行跳出循环
	    	}
       	//如果第一个前缀一样，那么index++，访问下一个字符。
	    	save+=compare;
	    	index++;
	    	compare=strs[0].charAt(index);
	    }
		}catch(IndexOutOfBoundsException e){//数组越界说明已经比较完毕，返回结果就可以
			return save;
	 	}
 }
}
```

# 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

```pseudocode
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

输入：digits = [0]
输出：[1]
```



思路：每次先加最高位，若为10，则清零，继续计算前一位。若为10的已经是第一个了，那么在最前面插入1，本位清零

语言：C++

```cpp
class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		bool flag = false;
		int i = digits.size() - 1;
		while (true != flag) {
      
			if (10 == ++digits[i])
			{
				digits[i] = 0;
				if (0 == i)
				{

					digits.insert(digits.begin(), 1);
					flag = true;
					break;
				}
				digits[i] = 0;
				i--;

			}
			else 
				flag = true;
			
		}
		return digits;
	}
};
```

# 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

```pseudocode
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```



思路：单纯遍历，暴力计算

语言：C++

```cpp
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target){
		for (int i = 0; i < nums.size(); i++)
		{
				for (int j = i+1; j < nums.size(); j++)
					if ((nums[i] + nums[j]) == target)
						return {i,j};
		}
        return {0,0};//如果没有，默认返回(0,0)
	}
};
```

# 卡牌分组

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

- 每组都有 X 张牌。
- 组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

```pseudocode
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

输入：[1]
输出：false
解释：没有满足要求的分组。

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]
```



语言：java

```java
class Solution{

	private int gcd(int a,int b) {
		return b==0?a: gcd(b,a%b);
	}
	
	
	public  boolean hasGroupsSizeX(int[] deck) {
		int a=-1;
		int[] save=new int[10000];
		for(int i:deck)
			save[i]++; //若deck的元素为i，则将save数组对应下标的元素++，以便统计数据
		for(int i:save)//求save数组，保存数据的最大公约数
		{
			if(a==-1)//设一个特殊flag，以便初始化数据
				a=i;
			else
				a=gcd(a,i);
		}
		if(a==1)
			return false;
		else
			return true;

	}
}
```

# 整数反转

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

```pseudocode
输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21
```



语言：java

```java
class Solution {
	public int reverse(int x) {
	int max = 0x7fffffff, min = 0x80000000;//int的最大值最小值
      int flag=0;
      long output=0;
      if(x<0){
    	  x=-x;
    	  flag++;
      }
       while(x!=0)
       {
    	   //System.out.println(output);
    	   output*=10;
    	   output+=x%10;
    	   x=x/10;
       }
       if(flag==1)
    	   output=-output;
       if(output>max||output<min)
    	   return 0;
       return (int)output;
    }
}
```

# 有效的括号

给定一个只包括 '('    ')'，'{'     '}'     '['    ']' 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

```pseudocode
输入: "()"
输出: true

输入: "([)]"
输出: false

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "{[]}"
输出: true
```





语言：java

```java
class Solution {
	public boolean isValid(String s) {
		char[] c=s.toCharArray();//转换为字符数组
		Stack stack=new Stack();
		for(int i=0;i<s.length();i++)
		{
		
			if (stack.empty()) {
			stack.push(c[i]);
			 continue;
			} 
			System.out.print((char)(c[i]+0));
			if( (char)stack.peek()+1== c[i]||
					(char)stack.peek()+2== c[i]
					
						) 
					stack.pop();	
			else
				stack.push(c[i]);
			
			
		}	
		return stack.empty();
    }
}
```

# 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

```pseudocode
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```



思路：每次把原来的数字x删去一位保存到另一个整数palindrome里面，直到把x删去一半为止。如果说是奇数位的话，比如说121，x最后会变成1，palindrome会变成12。如果是偶数位的话，那么两边应该是完全一样的。所以最后应该判断`palindrome==x||palindrome/10==x;`。

语言：java

```java
class Solution {
   	 public boolean isPalindrome(int x) {
	      if(x<0||x%10==0&&x!=0)//首先排除负数，和末尾为0的数，这两种肯定不是回文数
	        return false;
	      int palindrome=0;
       	//palindrome = palindrome*10+x%10就是每次把x的最后一位添加到palindrome后面
       	//然后把x消掉最后一位，直到palindrome大于或者等于x
        for(; palindrome<x; palindrome = palindrome*10+x%10,x/=10);

       //因为for循环出来以后，palindrome有可能大于等于x，所以要判断两种情况。
	      return palindrome==x||palindrome/10==x;
	    }
}
```

# 罗马数字转整数

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```pseudocode
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。



```pseudocode
输入: "III"
输出: 3

输入: "IV"
输出: 4

输入: "IX"
输出: 9

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

 

语言：java

```java
class Solution {
	 public int romanToInt(String s) {
	        char[] c= s.toCharArray();
	        int num=0;
	        for(int i=0;i<s.length();i++)
	        {
	        	switch(c[i]) {
	        	case 'I':num+=1;
	        		break;
	         	case 'V':num+=5;
        			break;
	         	case 'X':num+=10;
	         		break;
	         	case 'L':num+=50;
         			break;
	         	case 'C':num+=100;
         			break;
	         	case 'D':num+=500;
         			break;
	         	case 'M':num+=1000;
     				break;	
        		
	        	}
	        	if(i!=0 && (c[i]=='V'||c[i]=='X')&& c[i-1]=='I')
	        			num=num-2*1;
	        	if(i!=0 && (c[i]=='L'||c[i]=='C')&& c[i-1]=='X')
        			num=num-2*10;
	        	if(i!=0 && (c[i]=='D'||c[i]=='M')&& c[i-1]=='C')
        			num=num-2*100;
	        	
	        }
	        return num;
	    }
}
```

# 排序数组

给你一个整数数组 `nums`，请你将该数组升序排列。

```pseudocode
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
```



语言：java

```java
class Solution {
    void quickSort(int[] nums ,int left,int right){
		   if(right<=left)
        	return ;
		   int temp=nums[left];
		   int saveleft=left;
		   int saveright=right;
		   int flag=nums[left];
        while(right>left)
        {
        	while(right>left &&  nums[right]>=flag)
        		right--;
        	if(right>left)nums[left]=nums[right];
        	while(right>left &&  nums[left]<=flag)
        		left++;
        	if(right>left)nums[right]=nums[left];
        }
   
        nums[left]=temp;
    	
    	quickSort(nums,saveleft,right);
    	quickSort(nums,right+1,saveright);
    	
        
	}
	
	 public  int[] sortArray(int[] nums) {
	        
	        quickSort(nums,0,nums.length-1);
	        return nums;
	
    }
}
```

# 生命游戏

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

```pseudocode
输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```



语言：java

```java
class Solution {
	
	   public static void gameOfLife(int[][] board) {
  	int[][] saveBoard=new int[board.length+2][board[0].length+2];
  	for(int i=0;i<board.length;i++)
  		for(int j=0;j<board[0].length;j++)
  			saveBoard[i+1][j+1]=board[i][j];

  	int num=0;
  	
  	for(int i=0;i<board.length;i++) {
  		for(int j=0;j<board[0].length;j++)
  		{

  			num=num+saveBoard[i][j]+saveBoard[i][j+1]+saveBoard[i][j+2]+saveBoard[i+1][j]+saveBoard[i+1][j+2]
  					+saveBoard[i+2][j]+saveBoard[i+2][j+1]+saveBoard[i+2][j+2];
  					System.out.print(num+" ");
  			if(saveBoard[i+1][j+1]==1 && (num<2 ||num>3)  )
  				board[i][j]=0;
  			if(saveBoard[i+1][j+1]==0 && num==3)
				board[i][j]=1;
  			num=0;//归零，算下一个cell
  		}
   		
  	}
}
}
```



# 旋转矩阵

给你一幅由 `N × N` 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

```pseudocode
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]


给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```



思路：首先，不占用额外的内存空间，就需要使用异或的算法原地翻转，这个就是难点。剩下的倒不难，首先把数组按照对角线进行翻转，之后把数组进行左右对称。

语言：C++

```c++
class Solution {
public:
	void rotate(vector<vector<int>>& matrix) {
		int n = matrix.size();
    
		for(int i=0;i<n;i++)//对角线翻转
			for (int j = i+1; j < n ; j++)
			{
				matrix[i][j] = matrix[i][j] ^ matrix[j][i];
				matrix[j][i] = matrix[i][j] ^ matrix[j][i];
				matrix[i][j] = matrix[i][j] ^ matrix[j][i];
			}
    
		for(int i=0;i<n;i++)//左右翻转，
			for (int j = 0; j < n / 2; j++)
			{
        //n-1是实际长度，-j就是对应的对称列。
				matrix[i][j] = matrix[i][j] ^ matrix[i][n - j - 1];
				matrix[i][n - j - 1] = matrix[i][j] ^ matrix[i][n - j - 1];
				matrix[i][j] = matrix[i][j] ^ matrix[i][n - j - 1];
			}
	}
};
```

# 2的幂次方

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

```pseudocode
输入: 1
输出: true
解释: 20 = 1

输入: 16
输出: true
解释: 24 = 16
```



思路：需要明白一个重要算法，n&n-1会删掉该数二进制的最后一个1，比如说a=15，那么二进制就是1111。`a&a-1==1110`，就是这样子。2的幂次方在二进制中，一定是1开头后面全是0，所以如果对这个数使用这个算法，就可以很容易判断出来了。为0的数是幂次方，非0的数不是。

语言：c++

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0)
            return false;
        else if( (n&n-1)==0  )
            return true;
        else
            return false;
    }
};
```

