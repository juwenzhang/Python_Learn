# Python 的线程和进程

## 线程和进程的基本概念

> * **进程**是在**资源分配**的**最小单元**
> * **线程**是**CPU** 调度的**最小单位**
>
> ### **线程和进程之间的关系**
>
> * 一个线程只能有一个进程，一个进程可以有多个线程，每个进程至少有一个线程
> * 资源分配分配给进程，一个进程中的所有的线程共享其中的所有资源
> * 线程在执行过程中需要协同同步，不同进程间的线程需要利用消息同步机制来实现通讯
> * 真真执行任务的是我们的线程
> * 不同进程间的数据是很难实现共享的呐
> * 同一进程下，不同的线程之间资源共享
> * 创建进程消耗的资源大于创建新的线程占用的资源
> * 进程中不同的线程使用同一资源需要加锁，防止发生资源的抢夺的情形出现



## 串行 | 并行 | 并发

> 串行：就是说的是**做完一件事情后再执行下一件事情**，完成的任务时间为所有的任务的时间总和
>
> 并行：两个或者多个事件**在同一个时刻发生**，**相当于多个人同时完成多件事**，物理意义上的并行
>
> 并发：两个或者多个事件**在同一个时间间隔内发生**，**相当于一个人同时做多件事**，逻辑意义上的并行



## 线程

> ### python 中涉及到线程相关的模块总共有两个:
>
> * **_thread**: 这个就是一个pathon3 之前的一个重命名模块
> * **threading**: 我们的常使用的线程模块
>
> ### python 中如何创建线程呐？？？
>
> * 通过继承 Thread 类实现创建新的线程
> * 通过 Thread 类构造器来创建新线程
>
> **join方法**： 实现的就是让子线程阻塞主线程的执行过程，也就是说使用了 join 方法的子线程运行结束后再往下执行 
>
> `from threading import Thread`



### 锁的理解

> #### 锁的概念
>
> * **GIL** 就是**全局解析器锁**，任何的线程只有实现进行获取得到了这个锁之后才可以执行
>   * 就是因为这把锁的存在，实际上的话， python不管如何，一直只是一个线程在运行
> * **GIL** 全局解析器锁什么时候释放：
>   * 当当前的执行线程遇到了 IO 操作的时候，会主动放弃 GIL
>   * 当前执行的线程执行了 100 个字节码的时候，会自动释放 GIL 锁
>   * GIL 是一个粗粒度的锁，必须配合每个线程模块中的锁才可以对每个原子操作进行锁定
>   * 保证了对一个数据操作的正确性
>
> `from threading import Lock`
>
> `lock = Lock()`
>
> `lock.acquire()`  获取锁
>
> `lock.release()`  释放锁
>
> `with 语句` 来实现自动的获取锁和释放锁



### 消息队列进行 *线程* 间的通讯

> * **Event** : 主要是用于通过**事件通知机制实现线程的大规模并发**
> * **Condition**：主要是用于多个线程间接**轮流交替执行任务**
> * **Queue**：主要是用于不同线程间**任意类型数据的共享**



> * `q =  Queue(maxsize = 0)`
>   * maxsize 默认值为 0， 代表的是我们的消息队列的消息的个数不受限制
>   * maxsize > 0 ，就是说明的是我们的消息队列中的消息个数是受限制的，就是我们自己指定的这个数
>
> * `q.get()`  阻塞程序，等待队列消息
>
> * `q.get(timeout=1)` 阻塞队列，同时设置超时时间
>   * 设置加入消息队列的超时时间，这个在编程中经常看到
>
> * `q.put()`  发送消息，将消息放入队列



## 进程

> 创建进程的方式和创建线程的方式相同
>
> 都是含有两种方法的
>
> * 指定函数来实现创建进程
> * 继承 Process 类创建进程



## 线程和进程比较

> 多进程的优点以及缺点有那些：
>
> * 独立运行互不干扰
> * 创建进程的代价是十分大的，会导致电脑的占用十分大，导致出现运行卡顿问题
>
> 多线程的优点和缺点
>
> * 效率比较高，不会耗费大量的资源
> * 稳定性差，一个线程的崩溃，导致整个进程的崩溃

> 多进程的话使用于我们的计算的 CPU 密集型的任务
>
> 多线程的话适用于 IO 密集型的任务，比如说文件读取操作或者说爬虫的操作使用的比较多