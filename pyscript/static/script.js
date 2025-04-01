// Global variables
let currentUser = null;
let currentCourse = null;
const courses = [
    {
        id: 1,
        name: "Personal Branding Mastery",
        price: "₹635",
        originalPrice: "₹1,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. Emily Davis",
        mentorTitle: "PhD in Personal Branding",
        mentorBio: "10+ years experience helping professionals build powerful personal brands",
        lessons: 12,
        duration: "15 hours",
        level: "Beginner",
        description: "Learn how to build a powerful personal brand that attracts opportunities and establishes you as an authority in your field. This comprehensive course covers everything from defining your unique value proposition to creating a consistent online presence.",
        rating: 4.8,
        students: 1250,
        category: "Business"
    },
    {
        id: 2,
        name: "Soft Skills Excellence",
        price: "₹1,331",
        originalPrice: "₹3,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. Michael Brown",
        mentorTitle: "Leadership Development Expert",
        mentorBio: "Corporate trainer with 15+ years experience in Fortune 500 companies",
        lessons: 15,
        duration: "20 hours",
        level: "Intermediate",
        description: "Master the essential soft skills that will set you apart in any professional environment. This course covers communication, emotional intelligence, teamwork, and leadership skills that are crucial for career success.",
        rating: 4.9,
        students: 1850,
        category: "Business"
    },
    {
        id: 3,
        name: "Digital Marketing Pro",
        price: "₹2,499",
        originalPrice: "₹6,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. John Doe",
        mentorTitle: "Digital Marketing Strategist",
        mentorBio: "Helped 100+ businesses grow their online presence",
        lessons: 30,
        duration: "35 hours",
        level: "Intermediate",
        description: "Comprehensive digital marketing training covering SEO, social media, PPC, email marketing, and analytics. Learn strategies that actually work from an industry expert with proven results.",
        rating: 4.7,
        students: 3200,
        category: "Marketing"
    },
    {
        id: 4,
        name: "Data Science Fundamentals",
        price: "₹4,375",
        originalPrice: "₹12,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. Jane Smith",
        mentorTitle: "Senior Data Scientist",
        mentorBio: "10+ years in machine learning and data analysis",
        lessons: 25,
        duration: "40 hours",
        level: "Advanced",
        description: "Start your journey in data science with this comprehensive course covering Python, statistics, machine learning, and data visualization. Hands-on projects will help you build a strong portfolio.",
        rating: 4.9,
        students: 2800,
        category: "Technology"
    },
    {
        id: 5,
        name: "Financial Literacy Masterclass",
        price: "₹8,750",
        originalPrice: "₹24,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. Robert Johnson",
        mentorTitle: "Investment Banker",
        mentorBio: "20+ years in corporate finance and investments",
        lessons: 20,
        duration: "25 hours",
        level: "Intermediate",
        description: "Gain complete financial literacy covering personal finance, investing, retirement planning, and wealth building strategies. Learn from an industry veteran with decades of experience.",
        rating: 4.8,
        students: 1500,
        category: "Finance"
    },
    {
        id: 6,
        name: "AI for Business Leaders",
        price: "₹12,499",
        originalPrice: "₹34,999",
        image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1469&q=80",
        mentor: "Dr. Sarah Williams",
        mentorTitle: "AI Strategy Consultant",
        mentorBio: "Helping businesses implement AI solutions since 2010",
        lessons: 18,
        duration: "22 hours",
        level: "Advanced",
        description: "Understand how artificial intelligence is transforming industries and how you can leverage it for business growth. No technical background required - perfect for executives and entrepreneurs.",
        rating: 4.7,
        students: 950,
        category: "Technology"
    }
];

// Helper function to calculate discount percentage
function calculateDiscountPercentage(price, originalPrice) {
    try {
        const priceNum = parseFloat(price.replace(/[^0-9]/g, ''));
        const originalNum = parseFloat(originalPrice.replace(/[^0-9]/g, ''));
        if (originalNum > 0 && priceNum > 0) {
            return Math.round((1 - priceNum / originalNum) * 100);
        }
    } catch (e) {
        console.error('Error calculating discount', e);
    }
    return 0;
}

// Initialize the application
function initApp() {
    // Setup form event listeners
    document.getElementById('login-form')?.addEventListener('submit', handleLogin);
    document.getElementById('enroll-form')?.addEventListener('submit', handleEnrollment);
    document.getElementById('contact-form')?.addEventListener('submit', handleContact);
    
    // Password toggle
    document.getElementById('togglePassword')?.addEventListener('click', togglePasswordVisibility);
    document.getElementById('toggleEnrollPassword')?.addEventListener('click', toggleEnrollPasswordVisibility);
    
    // Start animations
    startTypewriter();
    setupScrollListener();
    
    // Check for remembered user
    const rememberedEmail = localStorage.getItem('rememberedEmail');
    if (rememberedEmail) {
        document.getElementById('login-email').value = rememberedEmail;
        document.getElementById('remember-me').checked = true;
    }
    
    // Test user for demo
    currentUser = {
        email: "test@example.com",
        name: "Test User",
        enrolledCourses: [1, 3]
    };
    
    // Initialize page based on URL hash or default to home
    const hash = window.location.hash.substring(1);
    const validPages = ['home', 'courses', 'about', 'contact', 'login'];
    const initialPage = validPages.includes(hash) ? hash : 'home';
    showPage(initialPage);
    
    // Setup navbar functionality
    setupNavbar();
}

// Setup navbar functionality
function setupNavbar() {
    // Mobile menu toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
    }
    
    // Close mobile menu when clicking a nav link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navbarCollapse?.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
            }
        });
    });
    
    // Add shadow to navbar on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 10) {
                navbar.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.15)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    }
    
    // Sticky navbar with smooth transition
    let lastScrollTop = 0;
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scroll down
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scroll up
            navbar.style.transform = 'translateY(0)';
        }
        lastScrollTop = scrollTop;
    });
    
    // Auto-hide navbar on mobile after click
    if (window.innerWidth < 992) {
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.navbar') && navbarCollapse?.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
            }
        });
    }
}

// Page navigation
function showPage(pageId) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.add('d-none');
    });
    
    // Show selected page
    const pageElement = document.getElementById(`${pageId}-page`);
    if (pageElement) {
        pageElement.classList.remove('d-none');
    }
    
    // Update URL hash
    window.location.hash = pageId;
    
    // Update active nav link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('onclick')?.includes(`'${pageId}'`)) {
            link.classList.add('active');
        }
    });
    
    // Special cases
    if (pageId === 'courses') {
        loadCourses();
    } else if (pageId === 'home') {
        window.scrollTo({top: 0, behavior: 'smooth'});
    }
    
    // Close mobile menu if open
    const navbarCollapse = document.querySelector('.navbar-collapse');
    if (navbarCollapse?.classList.contains('show')) {
        navbarCollapse.classList.remove('show');
    }
}

// Load courses into the courses page
function loadCourses() {
    const container = document.getElementById('course-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    courses.forEach(course => {
        const isEnrolled = currentUser?.enrolledCourses?.includes(course.id);
        const discountPercentage = course.originalPrice ? calculateDiscountPercentage(course.price, course.originalPrice) : 0;
        
        const col = document.createElement('div');
        col.className = 'col-md-6 col-lg-4 mb-4';
        col.innerHTML = `
            <div class="card course-card h-100">
                <div class="position-relative">
                    <img src="${course.image}" class="card-img-top course-img" alt="${course.name}" onerror="this.onerror=null; this.src='assets/courses/image copy.png'">
                    ${discountPercentage > 0 ? `<div class="position-absolute top-0 end-0 bg-danger text-white px-2 py-1 m-2 rounded">${discountPercentage}% OFF</div>` : ''}
                </div>
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <span class="badge bg-primary">${course.category}</span>
                        <div class="text-warning">
                            ${renderRatingStars(course.rating)}
                            <span class="text-muted ms-1">(${course.rating})</span>
                        </div>
                    </div>
                    <h5 class="card-title">${course.name}</h5>
                    <p class="card-text text-muted">${course.description.substring(0, 100)}...</p>
                    <div class="d-flex justify-content-between align-items-center mt-auto">
                        <div>
                            <span class="text-success fw-bold fs-5">${course.price}</span>
                            ${course.originalPrice ? `<span class="text-decoration-line-through text-muted ms-2">${course.originalPrice}</span>` : ''}
                        </div>
                        ${isEnrolled ? 
                            `<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i> Enrolled</span>` : 
                            `<button class="btn btn-sm btn-primary" onclick="prepareEnrollment(${course.id})">Enroll Now</button>`
                        }
                    </div>
                </div>
                <div class="card-footer bg-transparent border-top-0">
                    <button class="btn btn-outline-primary w-100" onclick="viewCourse(${course.id})">
                        <i class="bi bi-eye-fill me-2"></i> View Details
                    </button>
                </div>
            </div>
        `;
        container.appendChild(col);
    });
}

// Helper function to render rating stars
function renderRatingStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
    
    let stars = '';
    for (let i = 0; i < fullStars; i++) {
        stars += '<i class="bi bi-star-fill"></i>';
    }
    if (hasHalfStar) {
        stars += '<i class="bi bi-star-half"></i>';
    }
    for (let i = 0; i < emptyStars; i++) {
        stars += '<i class="bi bi-star"></i>';
    }
    return stars;
}

// View course details
function viewCourse(courseId) {
    currentCourse = courses.find(c => c.id == courseId);
    if (!currentCourse) return;
    
    // Update course info
    document.getElementById('course-title').textContent = currentCourse.name;
    document.getElementById('course-breadcrumb').textContent = currentCourse.name;
    document.getElementById('course-description').textContent = currentCourse.description;
    document.getElementById('course-price').textContent = currentCourse.price;
    document.getElementById('course-thumbnail').src = currentCourse.image;
    
    // Load lessons
    const lessonsContainer = document.getElementById('lessons-container');
    if (lessonsContainer) {
        lessonsContainer.innerHTML = '';
        
        for (let i = 1; i <= currentCourse.lessons; i++) {
            const isCompleted = currentUser?.enrolledCourses?.includes(currentCourse.id) && Math.random() > 0.7;
            
            const lessonDiv = document.createElement('a');
            lessonDiv.href = "#";
            lessonDiv.className = `list-group-item list-group-item-action lesson-item ${isCompleted ? 'completed' : ''}`;
            lessonDiv.innerHTML = `
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <h6 class="lesson-title mb-1">Lesson ${i}: ${currentCourse.name.split(' ')[0]} Concept ${i}</h6>
                        <small class="text-muted"><i class="bi bi-clock me-1"></i> ${Math.floor(Math.random() * 45) + 15} min</small>
                    </div>
                    <div>
                        <button class="btn btn-sm btn-outline-primary me-2" onclick="playVideo(${currentCourse.id}, ${i}, event)">
                            <i class="bi bi-play-circle me-1"></i> Preview
                        </button>
                        ${isCompleted ? 
                            '<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i> Completed</span>' : 
                            '<button class="btn btn-sm btn-success" onclick="markComplete(${currentCourse.id}, ${i}, event)">Mark Complete</button>'
                        }
                    </div>
                </div>
            `;
            lessonsContainer.appendChild(lessonDiv);
        }
    }
    
    // Load mentor info
    const mentorSection = document.getElementById('mentor-section');
    if (mentorSection) {
        mentorSection.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">About the Instructor</h5>
                <div class="d-flex">
                    <img src="assets/mentors/mentor-${currentCourse.id}.png" 
                         alt="${currentCourse.mentor}" 
                         class="mentor-img me-3"
                         onerror="this.onerror=null; this.src='https://randomuser.me/api/portraits/men/44.jpg'">
                    <div>
                        <h6>${currentCourse.mentor}</h6>
                        <p class="text-muted mb-1">${currentCourse.mentorTitle}</p>
                        <small class="text-muted">${currentCourse.mentorBio}</small>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Update enroll page with current course
    const enrollCourseName = document.getElementById('enroll-course-name');
    const enrollCoursePrice = document.getElementById('enroll-course-price');
    if (enrollCourseName) enrollCourseName.textContent = currentCourse.name;
    if (enrollCoursePrice) enrollCoursePrice.textContent = currentCourse.price;
    
    const enrollHero = document.querySelector('.enroll-hero');
    if (enrollHero) {
        enrollHero.style.backgroundImage = `linear-gradient(135deg, var(--primary), #224abe), url('${currentCourse.image}')`;
    }
    
    showPage('course-detail');
}

// Prepare enrollment from course detail page
function prepareEnrollmentFromDetail() {
    if (!currentCourse) return;
    prepareEnrollment(currentCourse.id);
}

// Prepare enrollment form
function prepareEnrollment(courseId) {
    const course = courses.find(c => c.id == courseId);
    if (!course) return;
    
    currentCourse = course;
    
    const enrollCourseName = document.getElementById('enroll-course-name');
    const enrollCoursePrice = document.getElementById('enroll-course-price');
    if (enrollCourseName) enrollCourseName.textContent = course.name;
    if (enrollCoursePrice) enrollCoursePrice.textContent = course.price;
    
    const enrollHero = document.querySelector('.enroll-hero');
    if (enrollHero) {
        enrollHero.style.backgroundImage = `linear-gradient(135deg, var(--primary), #224abe), url('${course.image}')`;
    }
    
    showPage('enroll');
}

// Handle login form submission
async function handleLogin(e) {
    e.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    const rememberMe = document.getElementById('remember-me').checked;
    const submitBtn = e.target.querySelector('button[type="submit"]');
    let originalText = '';
    
    if (!email || !password) {
        showMessage('Error', 'Please enter both email and password', 'error');
        return;
    }
    
    // Validate email format
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showMessage('Error', 'Please enter a valid email address', 'error');
        return;
    }
    
    try {
        // Show loading state
        originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Authenticating...';
        submitBtn.disabled = true;
        
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        if (password === 'password') { // Simple demo validation
            currentUser = {
                email: email,
                name: email.split('@')[0].replace('.', ' '),
                enrolledCourses: [1, 3] // Default enrolled courses for demo
            };
            
            if (rememberMe) {
                localStorage.setItem('rememberedEmail', email);
            } else {
                localStorage.removeItem('rememberedEmail');
            }
            
            showMessage('Login Successful', 'You have been logged in successfully!', 'success');
            showPage('courses');
        } else {
            showMessage('Login Failed', 'Invalid email or password', 'error');
        }
    } catch (error) {
        console.error('Login error:', error);
        showMessage('Error', 'Failed to login. Please try again.', 'error');
    } finally {
        if (submitBtn) {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }
    }
}

// Handle enrollment form submission
async function handleEnrollment(e) {
    e.preventDefault();
    const submitBtn = e.target.querySelector('button[type="submit"]');
    let originalText = '';
    
    const firstName = document.getElementById('enroll-first-name').value;
    const lastName = document.getElementById('enroll-last-name').value;
    const email = document.getElementById('enroll-email').value;
    const phone = document.getElementById('enroll-phone').value;
    const password = document.getElementById('enroll-password').value;
    const confirmPassword = document.getElementById('enroll-confirm-password').value;
    const paymentMethod = document.getElementById('enroll-payment-method').value;
    
    // Validate form
    if (!firstName || !lastName || !email || !phone || !password || !confirmPassword || !paymentMethod) {
        showMessage('Error', 'Please fill all required fields', 'error');
        return;
    }
    
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showMessage('Error', 'Please enter a valid email address', 'error');
        return;
    }
    
    if (!/^\d{10}$/.test(phone)) {
        showMessage('Error', 'Please enter a valid 10-digit phone number', 'error');
        return;
    }
    
    if (password !== confirmPassword) {
        showMessage('Error', 'Passwords do not match', 'error');
        return;
    }
    
    if (password.length < 8) {
        showMessage('Error', 'Password must be at least 8 characters', 'error');
        return;
    }
    
    if (!currentCourse) {
        showMessage('Error', 'No course selected', 'error');
        return;
    }
    
    try {
        // Show loading state
        originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Processing...';
        submitBtn.disabled = true;
        
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Create user account if not exists
        if (!currentUser) {
            currentUser = {
                email: email,
                name: `${firstName} ${lastName}`,
                enrolledCourses: [currentCourse.id]
            };
        } else if (!currentUser.enrolledCourses.includes(currentCourse.id)) {
            currentUser.enrolledCourses.push(currentCourse.id);
        }
        
        showMessage('Enrollment Successful', 
            `You have successfully enrolled in <strong>${currentCourse.name}</strong>!<br><br>
            Payment method: <strong>${paymentMethod}</strong><br>
            Amount paid: <strong>${currentCourse.price}</strong><br><br>
            You can now access the course from your dashboard.`, 
            'success'
        );
        
        // Clear form
        e.target.reset();
        
        // Redirect to course page
        setTimeout(() => {
            viewCourse(currentCourse.id);
        }, 3000);
    } catch (error) {
        console.error('Enrollment error:', error);
        showMessage('Error', 'Failed to complete enrollment. Please try again.', 'error');
    } finally {
        if (submitBtn) {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }
    }
}

// Handle contact form submission
function handleContact(e) {
    e.preventDefault();
    const name = document.getElementById('contact-name').value;
    const email = document.getElementById('contact-email').value;
    const subject = document.getElementById('contact-subject').value;
    const message = document.getElementById('contact-message').value;
    
    if (!name || !email || !message) {
        showMessage('Error', 'Please fill all required fields', 'error');
        return;
    }
    
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showMessage('Error', 'Please enter a valid email address', 'error');
        return;
    }
    
    // Simulate form submission
    setTimeout(() => {
        showMessage('Message Sent', 'Thank you for contacting us! We will get back to you within 24 hours.', 'success');
        e.target.reset();
    }, 1000);
}

// Toggle password visibility
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('login-password');
    const toggleBtn = document.getElementById('togglePassword');
    
    if (passwordInput && toggleBtn) {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            toggleBtn.innerHTML = '<i class="bi bi-eye-slash-fill"></i>';
        } else {
            passwordInput.type = 'password';
            toggleBtn.innerHTML = '<i class="bi bi-eye-fill"></i>';
        }
    }
}

function toggleEnrollPasswordVisibility() {
    const passwordInput = document.getElementById('enroll-password');
    const toggleBtn = document.getElementById('toggleEnrollPassword');
    
    if (passwordInput && toggleBtn) {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            toggleBtn.innerHTML = '<i class="bi bi-eye-slash-fill"></i>';
        } else {
            passwordInput.type = 'password';
            toggleBtn.innerHTML = '<i class="bi bi-eye-fill"></i>';
        }
    }
}

// Reset password function
function resetPassword() {
    const email = document.getElementById('login-email')?.value;
    
    if (!email) {
        showMessage('Reset Password', 'Please enter your email address to reset your password.', 'error');
        return;
    }
    
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showMessage('Error', 'Please enter a valid email address', 'error');
        return;
    }
    
    showMessage('Reset Link Sent', `We've sent a password reset link to <strong>${email}</strong>. Please check your inbox.`, 'success');
}

// Play video (simulated)
function playVideo(courseId, lessonNumber, event) {
    if (event) event.preventDefault();
    
    const course = courses.find(c => c.id == courseId);
    if (!course) return;
    
    showMessage('Video Preview', `Playing preview for Lesson ${lessonNumber} of <strong>${course.name}</strong>`, 'info');
}

// Mark lesson as complete
function markComplete(courseId, lessonNumber, event) {
    if (event) event.preventDefault();
    
    if (!currentUser) {
        showMessage('Error', 'Please login to track your progress', 'error');
        return;
    }
    
    const course = courses.find(c => c.id == courseId);
    if (!course) return;
    
    const lessonItem = event.target.closest('.lesson-item');
    if (lessonItem) {
        lessonItem.classList.add('completed');
        event.target.outerHTML = '<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i> Completed</span>';
        
        showMessage('Progress Updated', `Lesson ${lessonNumber} marked as complete!`, 'success');
    }
}

// Show message in modal
function showMessage(title, message, type = 'info') {
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');
    const modalHeader = document.querySelector('#messageModal .modal-header');
    
    if (!modalTitle || !modalBody || !modalHeader) return;
    
    modalTitle.textContent = title;
    modalBody.innerHTML = message;
    
    // Set color based on type
    if (type === 'error') {
        modalHeader.className = 'modal-header bg-danger text-white';
    } else if (type === 'success') {
        modalHeader.className = 'modal-header bg-success text-white';
    } else {
        modalHeader.className = 'modal-header bg-primary text-white';
    }
    
    // Show modal
    const modalElement = document.getElementById('messageModal');
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    }
}

// Typewriter effect for hero section
function startTypewriter() {
    const phrases = [
        "Elevate your career",
        "Learn from experts",
        "Gain practical skills",
        "Boost your income",
        "Achieve your goals"
    ];
    const element = document.getElementById('typewriter-text');
    if (!element) return;
    
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let isEnd = false;
    
    function type() {
        const currentPhrase = phrases[phraseIndex];
        
        if (isDeleting) {
            element.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
        } else {
            element.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
        }
        
        if (!isDeleting && charIndex === currentPhrase.length) {
            isEnd = true;
            isDeleting = true;
            setTimeout(type, 1500);
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            setTimeout(type, 500);
        } else {
            const speed = isDeleting ? 50 : isEnd ? 150 : 100;
            setTimeout(type, speed);
            isEnd = false;
        }
    }
    
    setTimeout(type, 1000);
}

// Setup scroll listener for back to top button
function setupScrollListener() {
    const backToTopBtn = document.querySelector('.back-to-top');
    if (!backToTopBtn) return;
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'flex';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    
    // Add click handler
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
}

// DOM Content Loaded1
document.addEventListener('DOMContentLoaded', initApp);