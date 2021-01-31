# 课程作业2函数
import numpy as np


def action2_fun():
    scoreType = np.dtype({'names': ['name', 'chinese', 'math', 'english', 'sum'],
                          'formats': ['U32', 'f', 'f', 'f', 'f']})
    score = np.array([("ZhangFei", 68, 65, 30, 0), ("GuanYu", 95, 76, 98, 0),
                      ("LiuBei", 98, 86, 88, 0), ("DianWei", 90, 88, 77, 0),
                      ("XuChu", 80, 90, 90, 0)], dtype=scoreType)
    # 各科平均成绩
    aveChines  = np.mean(score['chinese'])
    aveMath    = np.mean(score['math'])
    aveEnglish = np.mean(score['english'])
    print("Average Score: Chinese:", aveChines, " Math:", aveMath, " English:", aveEnglish)

    # 各科最小成绩
    minChines  = np.min(score['chinese'])
    minMath    = np.min(score['math'])
    minEnglish = np.min(score['english'])
    print("Min Score: Chinese:", minChines, " Math:", minMath, " English:", minEnglish)

    # 各科最大成绩
    maxChines  = np.max(score['chinese'])
    maxMath    = np.max(score['math'])
    maxEnglish = np.max(score['english'])
    print("Max Score: Chinese:", maxChines, " Math:", maxMath, " English:", maxEnglish)

    # 各科成绩标准差
    stdChines  = np.std(score['chinese'])
    stdMath    = np.std(score['math'])
    stdEnglish = np.std(score['english'])
    print("Std Score: Chinese:", stdChines, " Math:", stdMath, " English:", stdEnglish)

    # 各科成绩方差
    varChines  = np.var(score['chinese'])
    varMath    = np.var(score['math'])
    varEnglish = np.var(score['english'])
    print("Var Score: Chinese:", varChines, " Math:", varMath, " English:", varEnglish)

    # 个人成绩求和
    score['sum'] = -(score['chinese'] + score['math'] + score['english'])
    sortIdx = score['sum'].argsort()
    score['sum'] = -score['sum']
    print("Total Sort: ")
    for idx in sortIdx:
        print(score[idx]['name'], ": ", score[idx]['sum'])


if __name__ == '__main__':
    action2_fun()
