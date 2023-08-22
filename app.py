import streamlit as st

st.title('MelonShake Test')

st.sidebar.title('취향별 Playlist 생성')

select_type = st.sidebar.selectbox(
    '생성할 playlist를 선택해주세요',
    ['잔잔한','신나는','힐링','드라이브','운동','공부']
    )

