-- ============================================================
-- Day 1: Database Design and Table Creation
-- Name: Smrity Thapa
-- Approach: Create three new banking tables with proper
--           constraints, keys, and validation rules.
-- ============================================================


-- 1: Create banking.employees

CREATE TABLE banking.employees (
    employee_id  INT             PRIMARY KEY,
    branch_id    INT             NOT NULL REFERENCES banking.branches(branch_id),
    full_name    VARCHAR(100)    NOT NULL,
    email        VARCHAR(150)    NOT NULL UNIQUE,
    job_title    VARCHAR(50)     NOT NULL,
    salary       NUMERIC(12,2)   NOT NULL CHECK (salary > 0),
    hire_date    DATE            NOT NULL,
    is_active    BOOLEAN         NOT NULL DEFAULT TRUE
);


-- Task 2: Create banking.loans

CREATE TABLE banking.loans (
    loan_id       INT             PRIMARY KEY,
    customer_id   INT             NOT NULL REFERENCES banking.customers(customer_id),
    branch_id     INT             NOT NULL REFERENCES banking.branches(branch_id),
    loan_type     VARCHAR(20)     NOT NULL CHECK (loan_type IN ('HOME', 'AUTO', 'PERSONAL', 'BUSINESS')),
    loan_amount   NUMERIC(14,2)   NOT NULL CHECK (loan_amount > 0),
    interest_rate NUMERIC(5,2)    NOT NULL CHECK (interest_rate BETWEEN 0 AND 30),
    start_date    DATE            NOT NULL,
    end_date      DATE            NOT NULL CHECK (end_date > start_date),
    loan_status   VARCHAR(20)     NOT NULL DEFAULT 'ACTIVE' CHECK (loan_status IN ('ACTIVE', 'CLOSED', 'DEFAULTED'))
);


-- Task 3: Create banking.loan_payments

CREATE TABLE banking.loan_payments (
    payment_id      INT             PRIMARY KEY,
    loan_id         INT             NOT NULL REFERENCES banking.loans(loan_id),
    payment_amount  NUMERIC(12,2)   NOT NULL CHECK (payment_amount > 0),
    payment_date    DATE            NOT NULL,
    payment_method  VARCHAR(30)     NOT NULL CHECK (payment_method IN ('CASH', 'BANK_TRANSFER', 'CHEQUE', 'ONLINE')),
    payment_status  VARCHAR(20)     NOT NULL DEFAULT 'COMPLETED' CHECK (payment_status IN ('COMPLETED', 'PENDING', 'FAILED'))
);


-- Task 4: Test constraints (all should fail with errors)

-- This should fail because salary must be greater than zero (CHECK salary > 0).
INSERT INTO banking.employees (employee_id, branch_id, full_name, email, job_title, salary, hire_date)
VALUES (99, 1, 'Test Employee', 'test@bank.com', 'Accountant', -5000, '2024-01-01');

-- This should fail because 'STUDENT' is not in the allowed loan_type values.
INSERT INTO banking.loans (loan_id, customer_id, branch_id, loan_type, loan_amount, interest_rate, start_date, end_date)
VALUES (99, 1, 1, 'STUDENT', 100000, 10, '2025-01-01', '2027-01-01');

-- This should fail because customer_id = 9999 does not exist in banking.customers (foreign key violation).
INSERT INTO banking.loans (loan_id, customer_id, branch_id, loan_type, loan_amount, interest_rate, start_date, end_date)
VALUES (100, 9999, 1, 'HOME', 500000, 12, '2025-01-01', '2030-01-01');

-- This should fail because end_date is earlier than start_date (CHECK end_date > start_date).
INSERT INTO banking.loans (loan_id, customer_id, branch_id, loan_type, loan_amount, interest_rate, start_date, end_date)
VALUES (101, 1, 1, 'AUTO', 200000, 8, '2025-06-01', '2024-01-01');

-- This should fail because payment_amount must be greater than zero (CHECK payment_amount > 0).
INSERT INTO banking.loan_payments (payment_id, loan_id, payment_amount, payment_date, payment_method)
VALUES (99, 1, -1500, '2025-03-01', 'CASH');