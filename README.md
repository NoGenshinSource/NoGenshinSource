<h1 align="center">NoGenshinSource</h1>
<h3 align="center">Проект, который сделан на языке программировании Python. И это никак не относится к чему либо, автору делать нечего.</h3>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff) [![GitHub-Project](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NoGenshinSource/NoGenshinSource) [![License-apache](https://img.shields.io/hexpm/l/plug?style=for-the-badge)](./LICENSE)

## **Предупреждения(дисклеймер)**

Цель этого скрипта - предоставить возможность создать свой сервер другим путём, который ЯВЛЯЕТСЯ безопасным, но никак не заменой метаданных которые из-за них человек может отлететь в бан. Открытый код также есть на гитхабе, что даю понять о том, что и сам скрипт не содержит вируса или чего-либо(мало-ли). Также этот проект лишь запускает безопасный метод, КОТОРЫЙ НЕ ТРЕБУЕТ каких-либо замен файл и прочее. Если у вас появились проблемы с данным скриптом, то будьте добры написать это в обсуждениях, а что оставлять указано [тут](https://github.com/NoGenshinSource/NoGenshinSource/issues/1).

## Интро

Благодарю за скачивание скрипта "Genshin Private Start", и я сделал это ради скукоты и удобство, может это кому-то пригодится смотря на свою же точку зрения, вы можете так и использовать скрипт, а можете и не использовать. Автор скрипта не заставляет тех, кому-то запускать его если он(-а) создаёт себе приватный сервер в Геншине и хочет как-то по удобному его запустить.

И к тому же, я никак не заставляю тех или иных людей заставлять скачивать этот скрипт для использование приватного сервера в "Genshin Impact", и всё-же стоит отдать должное, что HoYoverse и MiHoYo запрещают использовать приватные сервера с цели чего-либо. И конечно же, они и сами виноваты, что проглядели этот момент или ещё что-то сделали. Но будьте честными и не используйте модификации на официальных играх. ;)
Вы конечно можете, но это уже смотря на ваше желание и так далее.

Благодарю за прочтение данного текста, и также перейдём к его использованию.

## Как использовать и обновлять скрипт?
Перед тем, как это всё использовать - убедитесь что у вас есть:
- Fiddler, javaDevelopmentKit(версия jdk-17.0.3.1), mongoDB.
- Python(Желательно версии 3.10, так как здесь присутствует махинация с match, питонисты поймут).
- WinRAR(Для клиента сервера).
- Клиент для 2.8: [1 архив](https://drive.google.com/file/d/1KeyK1WMy6XLyQ2IcyjCnN0LugQps4pMn/view) | [2 архив](https://drive.google.com/file/d/1U3VpiBTxWMZ05ghWsKOERqfnVU5BMKDV/view) | [3 архив](https://drive.google.com/file/d/1irQ8Iv9TderVZ8gEpBWEZqaCsUguF_lL/view)
- Прямые руки и мозги.

Теперь мы начинаем создавать наш сервер, но настоятельно рекомендуется вручную устанавливать программы как: Fiddler, javaDevelopmentKit(версия jdk-17.0.3.1), mongoDB. Советуется посмотреть это [видео](https://youtu.be/D_8o1Ik8NDQ?t=111) на моменте `1:51` чтобы вы "не тратили для себя слишком много времени". Дальше нам потребуется запустить Fiddler, затем же заходим в раздел `Tools` и `Options`, после чего мы нажимаем на `HTTPS` рядом с `General`, и затем ставил галочки как:
  - [X] Decrypt HTTPS traffic
  - [X] Ignore server ceritificate errors (unsafe)

После того как мы поставили эти галочки, рядом с `HTTPS` мы переходим в раздел `Connections` и меняем порт на `7777` лишь бы не `8888`. С этим мы разобрались, теперь нам потребуется заменить содержание скрипта, для этого мы переходим в `Rules` и выбираем `Customize rules` и заменяйте содержимое на вот это:
```java
import System;
import System.Windows.Forms;
import Fiddler;
import System.Text.RegularExpressions;

class Handlers
{
    static function OnBeforeRequest(oS: Session) {
        if(oS.host.EndsWith(".yuanshen.com") || oS.host.EndsWith(".yuanshen.com:8888") || oS.host.EndsWith(".hoyoverse.com") || oS.host.EndsWith(".mihoyo.com")) {
            oS.host = "localhost";
        }
    }
};
```
Затем после того как мы вставили скрипт, мы его сохраняем комбинации клавиш `Ctrl+S`, и всё - наш Fiddler настроен.

Теперь нам предстоит немного повозиться с Java, но так как мне впадлу этот процесс расписывать, то лучше уж посмотрите этот [фрагмент ролика](https://youtu.be/D_8o1Ik8NDQ?t=233), где более подробно расскажут об этом. Также советуется посмотреть и о MongoDB, чтобы сразу не тратить время на написание процесса...

Теперь мы распаковываем наш сервер и запускаем батник `install-requirements.cmd` для того, чтобы установить необходимые библиотеки для правильной работы скрипта. После того, как установились необходимые библиотеки мы ничего не трогаем из файлов, кроме `private-start.cmd` для самого запуска.
А тут всё просто, вам достаточно ничего не перетаскивать или ещё делать что-то, так как это готовый сервер с скриптом NoGenshinSource, дальше вам осталось открыть файл под названием `private-start.cmd` для запуска приложения и дальше вы нажмимаете на кнопку `Launch` для запуска сервера. А само название должен содержать как: `grasscutter-1.2.2-dev.jar`, но об этом не стоит переживать, так как это итак вставлено. И готово, а Геншин вам предстоит запустить из ярлыка `NoGenshinSource`, но вам нужно будет заменить путь к объекту. Нажмите ПКМ по ярлыку и затем выбираем "Свойства", дальше - мы вставляем в строке объект путь к клиенту, который вы ранее скачивали из архива и распаковали его где захотели(нам нужен именно его путь, чтобы запустился GenshinImpact.exe), и нажимаем на "ОК".

А чтобы обновить скрипт, вам потребуется открыть снова батник `private-start.cmd` если вы ранее запускали сервер при помощи его, но не закрыли текущий терминал. Далее мы нажимаем на кнопку где нарисована иконка "перезагрука", так как оно нам и нужно, нажимаем на него. Дальше программа самостоятельно сделает дело, и если обновление было найдено и успешно обновлено, то вам должно показаться окно с информацией об успешной функции самого скрипта. Это никак не затронет остальные файлы кроме NoGenshinSource.

Готово, вы теперь сможете играть в приватный сервер Genshin Impact, только не используйте на всякий свой настоящий аккаунт. А чтобы создать свой аккаунт, вам достаточно ввести `account create <ваш_никнейм> <любой_айди>`.

> P.S Если у вас случились какие-либо траблы со сервером приватного в Геншине, то обращайтесь в дискорд сервер который будет в ссылке из видео, там вам помогут, но в большинстве из случаев если вам попадётся ошибка связанное с сервером, а если вам показывает то что видео недоступно, то почитайте этот [мануал](https://guide.genshinnews.ml/troubleshooting.html) и не бесите администраторов там, ибо они не будут тратить большое количество нервов. Но лучше всего вам стоит пересмотреть или лучше всего посмотреть туториал как это сделать. Но в дальнейшем не бесите там админинистраторов, ведь они тоже люди как никак. :)
