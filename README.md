# CMS Rasa 3 - Hệ thống Quản lý Chatbot

Một hệ thống quản lý nội dung (CMS) toàn diện được thiết kế để quản lý và điều hành chatbot Rasa 3.x, bao gồm quản lý hội thoại, dữ liệu training và các tương tác của người dùng.

## 📋 Tổng quan dự án

CMS Rasa 3 là một nền tảng web hiện đại cho phép các nhà phát triển và quản trị viên:

- **Quản lý hội thoại**: Theo dõi, phân tích và quản lý các cuộc hội thoại giữa người dùng và chatbot
- **Quản lý dữ liệu training**: Tạo, chỉnh sửa và tối ưu hóa dữ liệu huấn luyện cho Rasa
- **Giám sát hiệu suất**: Theo dõi metrics và hiệu suất của chatbot trong thời gian thực
- **Quản lý intents và entities**: Giao diện trực quan để quản lý các intent và entity
- **Báo cáo và phân tích**: Dashboard chi tiết về hoạt động và hiệu suất chatbot

## 🚀 Tính năng chính

### 🔧 Quản lý Chatbot
- **Triển khai mô hình**: Upload và triển khai các mô hình Rasa đã được huấn luyện
- **Cấu hình chatbot**: Quản lý cấu hình, endpoints và các thông số của bot
- **Version control**: Theo dõi và quản lý các phiên bản khác nhau của mô hình

### 💬 Quản lý Hội thoại
- **Lịch sử chat**: Xem và tìm kiếm toàn bộ lịch sử hội thoại
- **Phân tích sentiment**: Đánh giá cảm xúc người dùng trong các cuộc hội thoại
- **Xuất dữ liệu**: Xuất dữ liệu hội thoại để phân tích hoặc backup

### 📊 Dữ liệu Training
- **Quản lý NLU data**: Tạo và chỉnh sửa dữ liệu huấn luyện NLU
- **Stories management**: Quản lý các story và rule cho dialogue management
- **Domain configuration**: Cấu hình domain với intents, entities, slots và responses
- **Training pipeline**: Giao diện để huấn luyện và đánh giá mô hình

### 📈 Analytics và Báo cáo
- **Dashboard tổng quan**: Hiển thị các metrics quan trọng
- **Báo cáo sử dụng**: Thống kê về frequency và patterns của người dùng
- **Performance metrics**: Accuracy, confidence scores và các chỉ số khác
- **User behavior**: Phân tích hành vi và preferences của người dùng

## 🛠️ Công nghệ sử dụng

### Backend
- **Python 3.8+**: Ngôn ngữ lập trình chính
- **FastAPI**: Framework web hiện đại và hiệu suất cao
- **SQLAlchemy**: ORM cho database management
- **PostgreSQL**: Database chính để lưu trữ dữ liệu
- **Redis**: Cache và session management
- **Rasa 3.x**: Framework chatbot chính

### Frontend
- **React.js**: Library frontend chính
- **TypeScript**: Typed JavaScript cho development tốt hơn
- **Material-UI**: Component library cho giao diện đẹp
- **Chart.js**: Visualization cho analytics và reports
- **Axios**: HTTP client cho API calls

### DevOps & Deployment
- **Docker**: Containerization
- **Docker Compose**: Multi-container deployment
- **nginx**: Reverse proxy và load balancer
- **GitHub Actions**: CI/CD pipeline

## 📦 Cài đặt và Thiết lập

### Yêu cầu hệ thống
- Python 3.8 hoặc cao hơn
- Node.js 16+ và npm
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose (tùy chọn)

### Cài đặt với Docker (Khuyến nghị)

```bash
# Clone repository
git clone https://github.com/dinhhuong2004/cms-rasa3.git
cd cms-rasa3

# Chạy với Docker Compose
docker-compose up -d

# Kiểm tra các services
docker-compose ps
```

### Cài đặt Manual

#### Backend Setup
```bash
# Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Cấu hình database
cp .env.example .env
# Chỉnh sửa file .env với thông tin database

# Chạy migrations
alembic upgrade head

# Khởi động server
uvicorn app.main:app --reload
```

#### Frontend Setup
```bash
cd frontend

# Cài đặt dependencies
npm install

# Chạy development server
npm start
```

## 🚀 Sử dụng

### Truy cập ứng dụng
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

### Workflow cơ bản

1. **Đăng nhập**: Sử dụng tài khoản admin để truy cập hệ thống
2. **Upload Rasa model**: Tải lên mô hình đã được huấn luyện
3. **Cấu hình chatbot**: Thiết lập endpoints và parameters
4. **Quản lý training data**: Thêm/sửa intents, entities và stories
5. **Theo dõi conversations**: Xem và phân tích các cuộc hội thoại
6. **Tối ưu hóa**: Sử dụng analytics để cải thiện chatbot

## 📚 API Documentation

API endpoints chính:

### Authentication
- `POST /auth/login` - Đăng nhập
- `POST /auth/logout` - Đăng xuất
- `GET /auth/me` - Thông tin user hiện tại

### Chatbot Management
- `GET /bots` - Danh sách chatbots
- `POST /bots` - Tạo chatbot mới
- `PUT /bots/{bot_id}` - Cập nhật cấu hình bot
- `POST /bots/{bot_id}/deploy` - Triển khai mô hình

### Conversations
- `GET /conversations` - Lịch sử hội thoại
- `GET /conversations/{conversation_id}` - Chi tiết hội thoại
- `POST /conversations/{conversation_id}/messages` - Gửi tin nhắn

### Training Data
- `GET /training/intents` - Danh sách intents
- `POST /training/intents` - Tạo intent mới
- `GET /training/stories` - Danh sách stories
- `POST /training/train` - Huấn luyện mô hình

## 🏗️ Cấu trúc dự án

```
cms-rasa3/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Core configuration
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic
│   │   └── utils/        # Utilities
│   ├── alembic/          # Database migrations
│   ├── tests/            # Backend tests
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API services
│   │   ├── store/        # State management
│   │   └── utils/        # Frontend utilities
│   ├── public/           # Static files
│   └── package.json      # Node dependencies
├── docker/               # Docker configurations
├── docs/                 # Documentation
├── scripts/              # Utility scripts
└── docker-compose.yml    # Multi-container setup
```

## 🧪 Testing

### Backend Tests
```bash
# Chạy tất cả tests
pytest

# Chạy với coverage
pytest --cov=app tests/

# Chạy specific test
pytest tests/test_api.py::test_create_bot
```

### Frontend Tests
```bash
cd frontend

# Chạy unit tests
npm test

# Chạy với coverage
npm test -- --coverage

# E2E tests
npm run test:e2e
```

## 📊 Monitoring và Logging

### Application Monitoring
- **Health checks**: `/health` endpoint cho monitoring
- **Metrics**: Prometheus metrics export
- **Logging**: Structured logging với JSON format
- **Error tracking**: Integration với Sentry (optional)

### Database Monitoring
- Connection pooling metrics
- Query performance tracking
- Database health monitoring

## 🔒 Bảo mật

### Authentication & Authorization
- JWT-based authentication
- Role-based access control (RBAC)
- API rate limiting
- CORS configuration

### Data Protection
- Password hashing với bcrypt
- Input validation và sanitization
- SQL injection protection
- XSS protection

## 🚀 Deployment

### Production Deployment
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d

# Monitor logs
docker-compose logs -f
```

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost/cms_rasa3
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Rasa
RASA_SERVER_URL=http://localhost:5005
RASA_TOKEN=your-rasa-token
```

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Để đóng góp:

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

### Development Guidelines
- Tuân thủ PEP 8 cho Python code
- Sử dụng ESLint và Prettier cho JavaScript/TypeScript
- Viết tests cho tất cả new features
- Update documentation khi cần thiết

## 📋 TODO & Roadmap

### Phase 1 (Current)
- [x] Project setup và cấu trúc cơ bản
- [ ] Authentication và user management
- [ ] Basic chatbot deployment
- [ ] Simple conversation tracking

### Phase 2
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Real-time conversation monitoring
- [ ] Automated testing cho Rasa models

### Phase 3
- [ ] Machine learning insights
- [ ] Advanced reporting
- [ ] Integration với external APIs
- [ ] Mobile app support

## 📞 Liên hệ & Hỗ trợ

- **Email**: dinhhuong2004@gmail.com
- **GitHub Issues**: [cms-rasa3/issues](https://github.com/dinhhuong2004/cms-rasa3/issues)
- **Documentation**: [Wiki pages](https://github.com/dinhhuong2004/cms-rasa3/wiki)

## 📄 License

Dự án này được phân phối dưới MIT License. Xem file `LICENSE` để biết thêm chi tiết.

---

**Lưu ý**: Dự án này đang trong giai đoạn phát triển. Các tính năng và API có thể thay đổi trong các phiên bản tương lai.