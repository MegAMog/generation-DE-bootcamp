--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5 (Debian 17.5-1.pgdg120+1)
-- Dumped by pg_dump version 17.5

-- Started on 2025-07-13 22:55:56 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16398)
-- Name: couriers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.couriers (
    courier_id integer NOT NULL,
    courier_first_name character varying NOT NULL,
    courier_last_name character varying NOT NULL,
    courier_phone_number character varying(11)
);


ALTER TABLE public.couriers OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16397)
-- Name: couriers_courier_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.couriers_courier_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.couriers_courier_id_seq OWNER TO postgres;

--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 219
-- Name: couriers_courier_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.couriers_courier_id_seq OWNED BY public.couriers.courier_id;


--
-- TOC entry 222 (class 1259 OID 16407)
-- Name: order_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_status (
    status_id integer NOT NULL,
    status_name character varying NOT NULL
);


ALTER TABLE public.order_status OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16406)
-- Name: order_status_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_status_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.order_status_status_id_seq OWNER TO postgres;

--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 221
-- Name: order_status_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_status_status_id_seq OWNED BY public.order_status.status_id;


--
-- TOC entry 224 (class 1259 OID 16418)
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    order_date date DEFAULT CURRENT_DATE,
    customer_first_name character varying NOT NULL,
    customer_last_name character varying NOT NULL,
    customer_address text NOT NULL,
    customer_phone_number character varying(11) NOT NULL,
    courier_id integer,
    order_status_id integer DEFAULT 1 NOT NULL,
    product_ids character varying NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16417)
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_order_id_seq OWNER TO postgres;

--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 223
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- TOC entry 218 (class 1259 OID 16386)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    product_id integer NOT NULL,
    product_name character varying NOT NULL,
    price numeric DEFAULT 0
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16385)
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_product_id_seq OWNER TO postgres;

--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 217
-- Name: products_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;


--
-- TOC entry 3227 (class 2604 OID 16401)
-- Name: couriers courier_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.couriers ALTER COLUMN courier_id SET DEFAULT nextval('public.couriers_courier_id_seq'::regclass);


--
-- TOC entry 3228 (class 2604 OID 16410)
-- Name: order_status status_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_status ALTER COLUMN status_id SET DEFAULT nextval('public.order_status_status_id_seq'::regclass);


--
-- TOC entry 3229 (class 2604 OID 16421)
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- TOC entry 3225 (class 2604 OID 16389)
-- Name: products product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);


--
-- TOC entry 3394 (class 0 OID 16398)
-- Dependencies: 220
-- Data for Name: couriers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.couriers (courier_id, courier_first_name, courier_last_name, courier_phone_number) FROM stdin;
1	John	Lennon	07123456789
2	Paul	McCartney	07345678923
3	George	Harrison	07345678901
4	Ringo	Starr	07345678456
\.


--
-- TOC entry 3396 (class 0 OID 16407)
-- Dependencies: 222
-- Data for Name: order_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_status (status_id, status_name) FROM stdin;
1	preparing
2	new
3	confirmed
4	out for delivery
5	delivered
6	cancelled
\.


--
-- TOC entry 3398 (class 0 OID 16418)
-- Dependencies: 224
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, order_date, customer_first_name, customer_last_name, customer_address, customer_phone_number, courier_id, order_status_id, product_ids) FROM stdin;
1	2025-07-13	Kate	Bush	23 King Way, London	07364563675	2	2	5
2	2025-07-13	Anna	Smith	46 Empire Way, London	07264163623	1	1	1,5,2
\.


--
-- TOC entry 3392 (class 0 OID 16386)
-- Dependencies: 218
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (product_id, product_name, price) FROM stdin;
1	espresso	3.5
2	americano	3.75
3	latte	3.75
4	cappuccino	3.25
5	flat white	3.5
6	macchiato	3.75
7	mocha	4.0
\.


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 219
-- Name: couriers_courier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.couriers_courier_id_seq', 4, true);


--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 221
-- Name: order_status_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_status_status_id_seq', 6, true);


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 223
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 2, true);


--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 217
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_product_id_seq', 7, true);


--
-- TOC entry 3237 (class 2606 OID 16405)
-- Name: couriers couriers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.couriers
    ADD CONSTRAINT couriers_pkey PRIMARY KEY (courier_id);


--
-- TOC entry 3239 (class 2606 OID 16414)
-- Name: order_status order_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_status
    ADD CONSTRAINT order_status_pkey PRIMARY KEY (status_id);


--
-- TOC entry 3241 (class 2606 OID 16416)
-- Name: order_status order_status_status_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_status
    ADD CONSTRAINT order_status_status_name_key UNIQUE (status_name);


--
-- TOC entry 3243 (class 2606 OID 16427)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- TOC entry 3233 (class 2606 OID 16394)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- TOC entry 3235 (class 2606 OID 16396)
-- Name: products products_product_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_product_name_key UNIQUE (product_name);


--
-- TOC entry 3244 (class 2606 OID 16428)
-- Name: orders orders_courier_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_courier_id_fkey FOREIGN KEY (courier_id) REFERENCES public.couriers(courier_id);


--
-- TOC entry 3245 (class 2606 OID 16433)
-- Name: orders orders_order_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_order_status_id_fkey FOREIGN KEY (order_status_id) REFERENCES public.order_status(status_id);


-- Completed on 2025-07-13 22:55:56 UTC

--
-- PostgreSQL database dump complete
--

