# Exchange_rate_mult

## 개요
- 예전에 만든 것 업데이트
- GUI, 웹 크롤링은 파이썬, 데이터 처리는 JAVA로 돌아감
1. JAVA로 data_analyzer를(실행파일 j_module.jar) 실행시키고 파이썬으로 user_d_collecter을 실행시키면 
2. 파이썬이 환율정보를 긁어와 confirm.txt에 저장하고 JAVA가 그걸 읽어서 처리한 결과를 analyzer_r.txt에 저장할 것이다.
3. 그러면 파이썬이 다시 analyzer.txt를 읽어 이를 인터페이스에 띄운다. 
4. 그리고 위의 과정이 일정 시간을 주기로 반복된다. 

## problems:
- 자바 실행파일과 파이썬 실행파일을 각각 실행시켜 동시에 돌아가도록 해야함.
- 둘 사이에 일종의 race가 발생하여 어느쪽이 먼저 실행될지, 양측이 동시에 파일에 접근시 발생하는 문제 -> 접근 주기 시간을 가능한 겹치지 않도록 설정했으나 근본적이지 않음
    

## maybe:
- 하나의 executable로 만들면 해결될 것\n
- 
