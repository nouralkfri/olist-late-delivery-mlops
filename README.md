# Late Delivery Prediction — Inference Service

نظام يتوقع هل طلب Olist رح يوصل متأخر أو بالوقت، مبني فوق موديل مدرب بالنوتبوكس.

## هيكلية المشروع

- `notebooks/` — النوتبوكس الستة (قراءة، label، split، EDA، features، تدريب)
- `src/` — كود الـ inference: predict.py (تحميل الموديل والتوقع)، validation.py (فحص المدخلات)، logger.py (تسجيل الطلبات)
- `app/` — خدمة FastAPI (main.py)
- `config/` — إعدادات المشروع (config.yaml) — كل المسارات من هون، ما في hardcoded paths
- `models/` — الموديل والـ scaler وقائمة الفيتشرز المحفوظة (متتبعة بـ DVC)
- `tests/` — اختبارات pytest
- `logs/` — سجلات كل طلب توقع (مدخل، مخرج، زمن)
- `.github/workflows/` — CI pipeline (تشغيل التيستات تلقائياً عند push)

## كيف تشغل المشروع من الصفر
