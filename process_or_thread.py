# -*-coding:utf-8-*-
# created by ChenWC on 2022-08-10 11:11
__author__ = "ChenWC"

from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


class ThreadExecutor:
    """
    多线程函数执行器，用于多线程执行任务
    """
    app = None  # 使用类变量来保存核心对象，这样每次使用多线程都要初始化实例，从而避免所有实例都共用一个fs的问题

    def __init__(self, thread_number):
        self.executor = ThreadPoolExecutor(thread_number)  # 初始化线程池
        self.fs = []

    def add_job(self, fn, *args, **kwargs):
        """
        启动子线程并将启动后的子线程保存到实例变量中
        """
        self.fs.append(self.executor.submit(fn, *args, curr_app=self.app, **kwargs))

    def job_done(self):
        """
        用于等待所有任务执行完成
        """
        wait(self.fs, return_when=ALL_COMPLETED)

    @property
    def job_results(self):
        """
        获取子线程执行结束的结果
        """
        results = {
            'success': [],
            'fail': []
        }
        with self.app.app_context():
            for func in self.fs:
                try:
                    results['success'].append(func.result())
                except Exception as e:
                    results['fail'].append(e)
        return results