def firstFunction(n, w, h):
    print("尊敬的 "+ n + " 先生/女士您好！")
    perfect = w / (h * h)
    if perfect < 18.5:
        print("您的BMI值为：%.2f，您的体重过轻！" % perfect)
    elif perfect >= 18.5 and perfect < 24:
        print("您的BMI值为：%.2f，您的体重正常！" % perfect)
    elif perfect >= 24 and perfect < 28:
        print("您的BMI值为：%.2f，您的体重过重！" % perfect)
    elif perfect >= 28 and perfect < 32:
        print("您的BMI值为：%.2f，您的体重肥胖！" % perfect)
    else:
        print("您的BMI值为：%.2f，您的体重严重肥胖！" % perfect)

    print("您的身高为：%.2f米，体重为：%.2f公斤" % (h, w))

# Call function
firstFunction("张三", 75, 1.75)

# Press any key to close
input("按任意键退出...")