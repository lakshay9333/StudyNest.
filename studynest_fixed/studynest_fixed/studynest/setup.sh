#!/bin/bash
# ─────────────────────────────────────────
#  StudyNest Setup Script
#  Run once: bash setup.sh
# ─────────────────────────────────────────

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🗄️  Creating database & tables..."
python manage.py migrate

echo "👤 Creating superuser for admin panel..."
echo "   (Username: admin  Password: admin123)"
echo "from core.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin','admin@studynest.com','admin123')" | python manage.py shell

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Start the server:  python manage.py runserver"
echo "🌐 Open browser:      http://127.0.0.1:8000"
echo "⚙️  Admin panel:       http://127.0.0.1:8000/admin  (admin / admin123)"
echo ""
echo "🔐 Chat gate code:    Set your own on first use"
echo "🔓 Message unlock:    Same as gate code"
echo ""
echo "🤖 AI Search setup (required for AI feature):"
echo "   export ANTHROPIC_API_KEY=your_key_here"
echo "   Then restart: python manage.py runserver"
echo "   Get a key at: https://console.anthropic.com"
