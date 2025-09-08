import requests
from collections import Counter

def main():
    print("=== Анализатор профиля GitHub ===")
    
    while True:
        try:
            # Запрос имени пользователя
            username = input("\nВведите имя пользователя GitHub: ").strip()
            
            if not username:
                print("Имя пользователя не может быть пустым!")
                continue
            
            # Получение данных с GitHub API
            url = f"https://api.github.com/users/{username}/repos"
            response = requests.get(url)
            
            # Обработка ошибок
            if response.status_code == 404:
                print(f"Ошибка: Пользователь '{username}' не найден")
                continue
            elif response.status_code == 403:
                print("Ошибка: Превышен лимит запросов. Попробуйте позже.")
                continue
            elif response.status_code != 200:
                print(f"Ошибка API: {response.status_code}")
                continue
            
            repos = response.json()
            
            # Анализ данных
            total_repos = len(repos)
            total_stars = sum(repo['stargazers_count'] for repo in repos)
            
            if repos:
                most_starred = max(repos, key=lambda x: x['stargazers_count'])
                most_starred_name = most_starred['name']
                most_starred_stars = most_starred['stargazers_count']
            else:
                most_starred_name = "Нет репозиториев"
                most_starred_stars = 0
            
            # Анализ языков программирования
            languages = []
            for repo in repos:
                if repo['language']:
                    languages.append(repo['language'])
            
            language_counter = Counter(languages)
            top_languages = language_counter.most_common()
            
            # Вывод результатов
            print(f"\nАналитика профиля GitHub: {username}")
            print("----------------------------------")
            print(f"- Количество публичных репозиториев: {total_repos}")
            print(f"- Общее количество звёзд: {total_stars}")
            print(f"- Самый популярный репозиторий: {most_starred_name} (⭐ {most_starred_stars})")
            
            if top_languages:
                print("- Топ языков программирования:")
                for lang, count in top_languages:
                    repo_word = "репозиторий" if count == 1 else "репозитория" if 2 <= count <= 4 else "репозиториев"
                    print(f"  - {lang}: {count} {repo_word}")
            else:
                print("- Языки программирования: не указаны")
                
        except requests.exceptions.RequestException:
            print("Ошибка сети: Проверьте подключение к интернету")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
        
        # Запрос на продолжение
        if input("\nПродолжить? (y/n): ").lower() not in ['y', 'yes']:
            break

if __name__ == "__main__":
    main()