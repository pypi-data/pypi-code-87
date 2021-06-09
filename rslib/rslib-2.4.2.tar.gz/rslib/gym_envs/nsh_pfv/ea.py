import numpy as np
import geatpy as ea


class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self, Dim):
        name = 'MyProblem' # 初始化name（函数名称，可以随意设置）
        M = 1 # 初始化M（目标维数）
        maxormins = [-1] # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        # Dim = 1 # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [-1] * Dim# 决策变量下界
        ub = [1] * Dim# 决策变量上界
        lbin = [1] * Dim # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop): # 目标函数
        x = pop.Phen # 得到决策变量矩阵
        pop.ObjV = x * np.sin(10 * np.pi * x) + 2.0 # 计算目标函数值，赋值给pop种群对象的ObjV属性
        pass


class solution(object):
    def __init__(self, problem=MyProblem(1)):
        self.problem = problem

    def run(self):
        """===============================实例化问题对象==========================="""
        problem = self.problem
        """=================================种群设置==============================="""
        Encoding = 'BG'       # 编码方式
        NIND = 4          # 种群规模
        Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders) # 创建区域描述器
        population = ea.Population(Encoding, Field, NIND) # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
        """===============================算法参数设置============================="""
        myAlgorithm = ea.soea_SEGA_templet(problem, population) # 实例化一个算法模板对象
        myAlgorithm.MAXGEN = 25 # 最大进化代数
        """==========================调用算法模板进行种群进化======================="""
        [population, obj_trace, var_trace] = myAlgorithm.run() # 执行算法模板
        population.save() # 把最后一代种群的信息保存到文件中
        # 输出结果
        best_gen = np.argmin(problem.maxormins * obj_trace[:, 1]) # 记录最优种群个体是在哪一代
        best_ObjV = obj_trace[best_gen, 1]
        print('最优的目标函数值为：%s'%(best_ObjV))
        print('最优的控制变量值为：')
        for i in range(var_trace.shape[1]):
            print(var_trace[best_gen, i])
        print('有效进化代数：%s'%(obj_trace.shape[0]))
        print('最优的一代是第 %s 代'%(best_gen + 1))
        print('评价次数：%s'%(myAlgorithm.evalsNum))
        print('时间已过 %s 秒'%(myAlgorithm.passTime))


if __name__ == '__main__':
    from nshpfv_env import NSHpfvEnv

    # observation =
    # while True:
    #     # if RENDER: env.render()
    #     action = RL.choose_action(observation)
    #     observation_, reward, done, info = env.step(action)  # reward = -1 in all cases

    class NSHpfvProblem(MyProblem): # 继承Problem父类
        def __init__(self):
            name = 'NSHpfvProblem' # 初始化name（函数名称，可以随意设置）
            self.env = NSHpfvEnv()
            self.env.reset()
            # 调用父类构造方法完成实例化
            MyProblem.__init__(self, 9)

        def aimFunc(self, pop): # 目标函数
            rewards=[]
            actions = pop.Phen # 得到决策变量矩阵
            for action in actions:
                _, reward, _, _ = self.env.step([action])
                rewards.append(reward[0])
                self.env.reset()
            pop.ObjV = np.array(rewards).reshape(-1,1)

    p = NSHpfvProblem()
    s = solution(p)
    s.run()