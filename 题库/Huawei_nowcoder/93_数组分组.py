"""
    题目描述:
        输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，
        并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），
        不是5的倍数也不是3的倍数能放在任意一组，可以将数组分为空数组，
        能满足以上条件，输出true；不满足时输出false。
    
    链接: https://www.nowcoder.com/practice/9af744a3517440508dbeb297020aca86?tpId=37&tqId=21316&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D4%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=4&judgeStatus=undefined&tags=&title=
"""

"""
    01-背包解法
    若物品重量为负，直接取绝对值，背包大小为绝对值总和即可
        1、若数的倍数是3或5,分别求和,记为S3和S5
        2、若数的倍数不是3或5,取绝对值,添加到'物品'数组里并求和,和记为Sn
        3、Sn加上S3与S5之差的绝对值
        4、取若干个'物品',如果能填满一半Sn,说明两组中各元素加起来的和相等
        5、dp[j]:装满重量为j的背包的方法数
"""

def findNum(nums: list[int], target: int) -> bool


def isDivided(nums: list[int]) -> bool:
    """
        分析:
            数组中的元素可能为负数，注意对负数的处理
            数组中的元素可能为负数，因此不符合01背包的应用场景；

            进一步分析，3的倍数为一堆，5的倍数为另一堆，因此要在剩下的元素中找到数字和满足:
                sum3 + x = sum5 + y -> x - y = sum5 - sum3
                x + y = sum_candidates
                因此， x = (sum_candidates + sum5 - sum3) / 2
            
            这里有个 bug， 公倍数的处理，不过应该是不存在公倍数

            设dp(j,i)表示能否从nums中下标i到n-1选取若干个元素，使它们的和为j的解。有解为true，无则false。 
            那么就可以写出递归关系： 
                dp(j,i) = dp(j,i+1)||dp(j-nums[i],i+1). 
            
            简单解释一下，若第i个元素不选，则dp(j,i) = dp(j,i+1)；
            若第i个元素选取，则dp(j,i) = dp(j-nums[i],i+1)； 
            
            那么边界条件就应该是： 
                当j=0,dp(j,i)=true; 当j=nums中下标i到n-1中任意个元素,dp(j,i)=true; 
                当i=n-1时，若nums[n-1]=j,则dp(j,i)=true;否则，dp(j,i)=false。
    """
    sum3, sum5, candidates = 0, 0, []
    for num in nums:
        if num % 3 == 0:
            sum3 += num
        elif num % 5 == 0:
            sum5 += num
        else:
            candidates.append(num)
    
    if (sum(candidates)+sum5-sum3) % 2 != 0:
        return False
    
    target = (sum(candidates)+sum5-sum3) / 2
    # 接下来的任务就是从 candidates 中找到数使其和为 target


if __name__ == "__main__":
    n = int(input(""))
    nums = list(map(int, input("").split()))

    
