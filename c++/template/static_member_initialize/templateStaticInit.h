class CMsgHdl
{
public:
	int m;
public:
	void handlemsg() {
		printf("handle complete!\n");
	}

};



template<class MessageHandlerClass>
class TimerApp
{
	//friend class TimerApp;
	typedef void (MessageHandlerClass::*HandlerMethod)();

public:
	static void AddTimer(int interval,MessageHandlerClass *handler){
		interval_ = interval;
		handler_ = handler;
	}
	static void AddMethod(HandlerMethod method)
	{
		handler_method_ = method;
	}
	int GetInterval() {return interval_;}

	void execute()
	{
		(handler_->*handler_method_)();
	}
	

private:
	static int interval_;
	static HandlerMethod handler_method_;    //�ص�����ָ��
	static MessageHandlerClass* handler_;    //���ö���
	static void OnTimer();
};


template<class MessageHandlerClass> int TimerApp<MessageHandlerClass>::interval_ = 0;
template<class MessageHandlerClass> MessageHandlerClass* TimerApp<MessageHandlerClass>::handler_ = 0;

// ����
//template<class MessageHandlerClass> TimerApp<MessageHandlerClass>::HandlerMethod TimerApp<MessageHandlerClass>::handler_method_ = &TimerApp<MessageHandlerClass>::AddTimer;

// δ����AddMethodʱ����ͨ��,����֮���޷�ͨ������
//template<class MessageHandlerClass> typename MessageHandlerClass::HandlerMethod TimerApp<MessageHandlerClass>::handler_method_ = 0;

// ����ͨ��
template<class MessageHandlerClass> typename TimerApp<MessageHandlerClass>::HandlerMethod TimerApp<MessageHandlerClass>::handler_method_ = 0; 