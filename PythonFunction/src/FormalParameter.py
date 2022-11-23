def Test(obj):
    '''
    obj: string || int (用于测试的对象)
    '''
    print("原有内容: ", obj)
    obj += obj
    print("修改后内容: ", obj)

# cn: 传递值 => 不可变对象 => 不改变形式参数的值
# cn: 引用传递 => 可变对象 => 改变形式参数的值

# en: Pass by value => immutable object => not change the value of formal parameter
# en: Pass by reference => mutable object => change the value of formal parameter

# jp: 値渡し => 不変オブジェクト => 形式パラメータの値を変更しない
# jp: 参照渡し => 可変オブジェクト => 形式パラメータの値を変更する

# cn: 传递值 || en: Pass by value || jp: 値渡し
print("=" * 10, "传递值", "=" * 10)
par = "Hello World!"
Test(par)

# cn: 引用传递 || en: Pass by reference || jp: 参照渡し
print("=" * 10, "引用传递", "=" * 10)
array = ["一体", "二极", "四象", "八卦"]
Test(array)

# cn: 点击任意键退出 || en: Press any key to close || jp: 任意のキーを押して終了
input("Press any key to close...")