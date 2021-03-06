"""
1117.H2O生成
现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。

存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。

氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。

这些线程应该三三成组突破屏障并能立即组合产生一个水分子。

你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。

换句话说:
如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
书写满足这些限制条件的氢、氧线程同步代码。

示例 1:
输入: "HOH"
输出: "HHO"
解释: "HOH" 和 "OHH" 依然都是有效解。

示例 2:
输入: "OOHHHH"
输出: "HHOHHO"
解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。

提示：
输入字符串的总长将会是 3n, 1 ≤n≤ 50；
输入字符串中的 “H” 总数将会是 2n 。
输入字符串中的 “O” 总数将会是 n 。
"""
from typing import Callable
from threading import Lock, Thread
import time
import threading


class H2O(object):
    def __init__(self):
        self.O = threading.Semaphore(1)
        self.H = threading.Semaphore(2)
        self.H_num = 0

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.H.acquire()
        releaseHydrogen()

        self.H_num += 1
        if self.H_num > 1:
            self.H_num -= 2
            self.O.release()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.O.acquire()
        releaseOxygen()
        self.H.release()
        self.H.release()


class H2O1:
    def __init__(self):
        self.h = 0
        self.o = 0
        self.h2o_thread = Thread(target=self.h2o, args=())
        self.h2o_thread.setDaemon(True)
        self.h2o_thread.start()
        self.h_lock = Lock()
        self.o_lock = Lock()
        self.hl = Lock()
        self.ol = Lock()
        pass

    def h2o(self):
        while True:
            if self.h >= 2 and self.o >= 1:
                self.h -= 2
                self.o -= 1
            time.sleep(0.01)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_lock.acquire()
        while self.h >= 2:
            time.sleep(0.01)
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h += 1
        self.h_lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        while self.o >= 1:
            time.sleep(0.01)
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o += 1
        self.o_lock.release()

