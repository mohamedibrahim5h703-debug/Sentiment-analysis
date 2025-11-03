# Sentiment-analysis
تطوير تطبيق Python على الويب باستخدام Flask ودمج مكتبات Watson AI القابلة للتضمين لجعل تطبيق الويب يعرض القدرات القائمة على الذكاء الاصطناعي.# مشروع تحليل المشاعر باستخدام Watson NLP و Flask

## خطوات التشغيل
1. تثبيت المكتبات:
   pip install -r requirements.txt

2. إعداد مفتاح Watson و URL في app/emotion_detector.py

3. تشغيل Flask:
   python server.py

4. اختبار واجهة POST:
   Endpoint: /analyze
   JSON body: {"text": "I love AI!"}

